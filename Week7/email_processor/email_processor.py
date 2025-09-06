from typing import List, Dict, Optional, Annotated
from datetime import datetime
import json
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, EmailStr, Field
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from langdetect import detect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import sqlite3
from email_validator import validate_email, EmailNotValidError

# Initialize MCP server
mcp = FastMCP("email_processor")

# Initialize OpenAI client
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Models
class EmailThread(BaseModel):
    """Email thread model"""
    thread_id: str
    subject: str
    emails: List[Dict]
    customer_id: str
    department: Optional[str] = None
    priority: int = 1
    status: str = "new"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class EmailAnalysis(BaseModel):
    """Email analysis results"""
    language: str
    sentiment_score: float
    urgency: int
    category: str
    key_points: List[str]
    suggested_department: str
    action_items: List[str]
    response_tone: str

# Database setup
def init_db():
    conn = sqlite3.connect(os.getenv('DATABASE_NAME', 'email_threads.db'))
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS email_threads (
            thread_id TEXT PRIMARY KEY,
            subject TEXT,
            customer_id TEXT,
            department TEXT,
            priority INTEGER,
            status TEXT,
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            thread_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper Functions
async def analyze_sentiment(text: str) -> float:
    """Analyze text sentiment using VADER"""
    scores = sentiment_analyzer.polarity_scores(text)
    return scores['compound']

async def detect_language(text: str) -> str:
    """Detect text language"""
    try:
        return detect(text)
    except:
        return 'en'

async def extract_action_items(text: str) -> List[str]:
    """Extract action items using GPT-4"""
    response = await client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                "role": "system",
                "content": "Extract actionable items from this email as a JSON list."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content).get('action_items', [])

# Database operations
def store_thread(thread: EmailThread):
    """Store thread in database"""
    conn = sqlite3.connect(os.getenv('DATABASE_NAME', 'email_threads.db'))
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO email_threads
        (thread_id, subject, customer_id, department, priority, status, created_at, updated_at, thread_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        thread.thread_id,
        thread.subject,
        thread.customer_id,
        thread.department,
        thread.priority,
        thread.status,
        thread.created_at.isoformat(),
        thread.updated_at.isoformat(),
        json.dumps(thread.dict())
    ))
    conn.commit()
    conn.close()

def get_thread(thread_id: str) -> Optional[EmailThread]:
    """Get thread from database"""
    conn = sqlite3.connect(os.getenv('DATABASE_NAME', 'email_threads.db'))
    c = conn.cursor()
    c.execute('SELECT thread_data FROM email_threads WHERE thread_id = ?', (thread_id,))
    result = c.fetchone()
    conn.close()
    
    if result:
        thread_data = json.loads(result[0])
        return EmailThread(**thread_data)
    return None

def get_all_threads() -> List[EmailThread]:
    """Get all threads from database"""
    conn = sqlite3.connect(os.getenv('DATABASE_NAME', 'email_threads.db'))
    c = conn.cursor()
    c.execute('SELECT thread_data FROM email_threads')
    results = c.fetchall()
    conn.close()
    
    return [EmailThread(**json.loads(row[0])) for row in results]

# MCP Tools
@mcp.tool()
async def process_email_thread(
    thread_id: str,
    subject: str,
    emails: List[dict],
    customer_id: str
) -> dict:
    """Process entire email thread with context
    
    Args:
        thread_id: Unique thread identifier
        subject: Email subject
        emails: List of email messages in thread
        customer_id: Customer identifier
    """
    # Combine all email content for analysis
    full_content = "\n".join([email['content'] for email in emails])
    
    # Perform comprehensive analysis
    analysis = EmailAnalysis(
        language=await detect_language(full_content),
        sentiment_score=await analyze_sentiment(full_content),
        urgency=len([e for e in emails if "urgent" in e['content'].lower()]) + 1,
        category=await categorize_thread(full_content),
        key_points=await extract_key_points(full_content),
        suggested_department=await determine_department(full_content),
        action_items=await extract_action_items(full_content),
        response_tone="formal" if await analyze_sentiment(full_content) < 0 else "friendly"
    )
    
    # Create thread object
    thread = EmailThread(
        thread_id=thread_id,
        subject=subject,
        emails=emails,
        customer_id=customer_id,
        department=analysis.suggested_department,
        priority=analysis.urgency,
        status="new"
    )
    
    # Store in database
    store_thread(thread)
    
    return {
        "thread": thread.dict(),
        "analysis": analysis.dict()
    }

@mcp.tool()
async def generate_multilingual_response(
    thread_id: str,
    language: str,
    tone: str = "professional"
) -> str:
    """Generate response in specified language with tone control
    
    Args:
        thread_id: Thread to respond to
        language: Target language code
        tone: Response tone (professional/friendly/formal)
    """
    thread = get_thread(thread_id)
    if not thread:
        return "Thread not found"
    
    response = await client.chat.completions.create(
        model=os.getenv('GPT_MODEL', 'gpt-4-turbo-preview'),
        messages=[
            {
                "role": "system",
                "content": f"""Generate an email response in {language}.
                Tone should be {tone}.
                Previous thread context will be provided."""
            },
            {
                "role": "user",
                "content": f"""Thread subject: {thread.subject}
                Latest email: {thread.emails[-1]['content']}
                Department: {thread.department}
                Priority: {thread.priority}"""
            }
        ]
    )
    
    return response.choices[0].message.content

@mcp.tool()
async def create_action_items(thread_id: str) -> List[dict]:
    """Extract and prioritize action items from email thread
    
    Args:
        thread_id: Thread to analyze
    """
    thread = get_thread(thread_id)
    if not thread:
        return []
    
    # Extract action items from full thread
    full_content = "\n".join([email['content'] for email in thread.emails])
    action_items = await extract_action_items(full_content)
    
    # Prioritize items
    prioritized_items = []
    for item in action_items:
        priority = thread.priority  # Use thread priority as base
        prioritized_items.append({
            "item": item,
            "priority": priority,
            "assigned_to": thread.department,
            "due_date": datetime.utcnow().isoformat()
        })
    
    return prioritized_items

@mcp.tool()
async def update_thread_status(
    thread_id: str,
    status: str,
    resolution_notes: Optional[str] = None
) -> dict:
    """Update email thread status
    
    Args:
        thread_id: Thread to update
        status: New status
        resolution_notes: Optional notes about resolution
    """
    thread = get_thread(thread_id)
    if not thread:
        return {"error": "Thread not found"}
    
    thread.status = status
    thread.updated_at = datetime.utcnow()
    
    if resolution_notes:
        thread.emails.append({
            "type": "note",
            "content": resolution_notes,
            "timestamp": datetime.utcnow().isoformat()
        })
    
    store_thread(thread)
    
    return {"thread_id": thread_id, "status": status}

@mcp.tool()
async def search_similar_threads(
    thread_id: str,
    limit: int = 5
) -> List[dict]:
    """Find similar previous email threads
    
    Args:
        thread_id: Current thread ID
        limit: Maximum number of similar threads to return
    """
    current_thread = get_thread(thread_id)
    if not current_thread:
        return []
    
    # Get all threads for comparison
    all_threads = get_all_threads()
    
    # Calculate similarity scores using GPT-4
    similar_threads = []
    for thread in all_threads:
        if thread.thread_id != thread_id:
            # Compare subjects and content
            similarity_response = await client.chat.completions.create(
                model=os.getenv('GPT_MODEL', 'gpt-4-turbo-preview'),
                messages=[
                    {
                        "role": "system",
                        "content": "Compare these two threads and return a similarity score between 0 and 1 as a JSON number."
                    },
                    {
                        "role": "user",
                        "content": f"""Thread 1: {current_thread.subject}\n{current_thread.emails[-1]['content']}
                        Thread 2: {thread.subject}\n{thread.emails[-1]['content']}"""
                    }
                ],
                response_format={ "type": "json_object" }
            )
            
            similarity = float(json.loads(similarity_response.choices[0].message.content).get('similarity', 0))
            
            if similarity > 0.5:  # Threshold for similarity
                similar_threads.append({
                    "thread_id": thread.thread_id,
                    "subject": thread.subject,
                    "similarity": similarity,
                    "resolution": thread.status == "resolved"
                })
    
    # Sort by similarity and return top matches
    similar_threads.sort(key=lambda x: x['similarity'], reverse=True)
    return similar_threads[:limit]

async def categorize_thread(content: str) -> str:
    """Categorize thread content"""
    response = await client.chat.completions.create(
        model=os.getenv('GPT_MODEL', 'gpt-4-turbo-preview'),
        messages=[
            {
                "role": "system",
                "content": "Categorize this email content into one category: technical, billing, account, general"
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return response.choices[0].message.content.strip().lower()

async def determine_department(content: str) -> str:
    """Determine appropriate department"""
    response = await client.chat.completions.create(
        model=os.getenv('GPT_MODEL', 'gpt-4-turbo-preview'),
        messages=[
            {
                "role": "system",
                "content": "Determine the appropriate department: support, billing, technical, general"
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return response.choices[0].message.content.strip().lower()

async def extract_key_points(content: str) -> List[str]:
    """Extract key points from content"""
    response = await client.chat.completions.create(
        model=os.getenv('GPT_MODEL', 'gpt-4-turbo-preview'),
        messages=[
            {
                "role": "system",
                "content": "Extract the main points from this email as a JSON list"
            },
            {
                "role": "user",
                "content": content
            }
        ],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content).get('key_points', [])

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
