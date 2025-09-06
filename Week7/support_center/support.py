from typing import Any, List, Optional
from datetime import datetime
import httpx
import os
import json
from mcp.server.fastmcp import FastMCP
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("support_center")

# Initialize OpenAI client
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Constants
TICKET_DB = {}  # In-memory storage for demo purposes

class Ticket:
    def __init__(self, customer_id: str, subject: str, description: str):
        self.id = len(TICKET_DB) + 1
        self.customer_id = customer_id
        self.subject = subject
        self.description = description
        self.status = "new"
        self.created_at = datetime.utcnow()
        self.messages = []
        self.analysis = {}

async def analyze_content(content: str) -> dict:
    """Helper function to analyze content using OpenAI's GPT-4"""
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a customer support analyst. Analyze the support ticket and provide structured analysis."
            },
            {
                "role": "user",
                "content": f"""Analyze this support ticket content:
                {content}
                
                Provide analysis in JSON format with these exact keys:
                - sentiment (positive/negative/neutral)
                - urgency (high/medium/low)
                - category (billing/technical/account/general)
                - key_points (array of max 3 points)"""
            }
        ],
        response_format={ "type": "json_object" }
    )
    
    return json.loads(response.choices[0].message.content)

@mcp.tool()
async def create_ticket(customer_id: str, subject: str, description: str) -> str:
    """Create a new support ticket.
    
    Args:
        customer_id: Unique identifier for the customer
        subject: Brief description of the issue
        description: Detailed description of the problem
    """
    # Create new ticket
    ticket = Ticket(customer_id, subject, description)
    
    # Analyze ticket content
    analysis = await analyze_content(f"{subject}\n{description}")
    ticket.analysis = analysis
    
    # Store ticket
    TICKET_DB[ticket.id] = ticket
    
    return f"""Ticket #{ticket.id} created successfully.
    Analysis:
    - Sentiment: {analysis.get('sentiment')}
    - Urgency: {analysis.get('urgency')}
    - Category: {analysis.get('category')}
    - Key points: {', '.join(analysis.get('key_points', []))}
    """

@mcp.tool()
async def add_message(ticket_id: int, message: str, is_customer: bool = True) -> str:
    """Add a message to an existing ticket.
    
    Args:
        ticket_id: The ID of the ticket to update
        message: The message content
        is_customer: Whether the message is from the customer (True) or agent (False)
    """
    if ticket_id not in TICKET_DB:
        return f"Error: Ticket #{ticket_id} not found"
    
    ticket = TICKET_DB[ticket_id]
    
    # Add message to ticket
    ticket.messages.append({
        "content": message,
        "sender": "customer" if is_customer else "agent",
        "timestamp": datetime.utcnow()
    })
    
    # If customer message, analyze and generate response
    if is_customer:
        analysis = await analyze_content(message)
        
        # Generate automated response based on analysis
        response = await generate_response(ticket, message, analysis)
        
        # Add automated response
        ticket.messages.append({
            "content": response,
            "sender": "agent",
            "timestamp": datetime.utcnow()
        })
        
        return f"""Message added and analyzed.
        Auto-response generated:
        {response}"""
    
    return "Message added successfully"

@mcp.tool()
async def get_ticket_status(ticket_id: int) -> str:
    """Get the current status and history of a ticket.
    
    Args:
        ticket_id: The ID of the ticket to check
    """
    if ticket_id not in TICKET_DB:
        return f"Error: Ticket #{ticket_id} not found"
    
    ticket = TICKET_DB[ticket_id]
    
    # Format message history
    messages = "\n".join([
        f"{msg['sender']} ({msg['timestamp']}): {msg['content']}"
        for msg in ticket.messages
    ])
    
    return f"""Ticket #{ticket_id} Status:
    Customer: {ticket.customer_id}
    Subject: {ticket.subject}
    Status: {ticket.status}
    Created: {ticket.created_at}
    
    Message History:
    {messages}
    """

async def generate_response(ticket: Ticket, message: str, analysis: dict) -> str:
    """Helper function to generate automated responses using GPT-4"""
    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a professional and empathetic customer support agent. Generate a helpful response."
            },
            {
                "role": "user",
                "content": f"""Generate a response to this customer message:
                
                Ticket Subject: {ticket.subject}
                Customer Message: {message}
                
                Analysis:
                - Sentiment: {analysis.get('sentiment')}
                - Urgency: {analysis.get('urgency')}
                - Category: {analysis.get('category')}
                
                Generate a professional and empathetic response:"""
            }
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
