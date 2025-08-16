import json
import os
from typing import Dict, List, Optional

import requests
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("⚠️  Warning: OPENAI_API_KEY not found in environment variables")
    print("Please set your OpenAI API key in a .env file or environment variable")
    exit(1)

# Set your OpenAI API key here or set it as an environment variable
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

class WebsiteAnalyzer:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini")
        self.roles = {
            "1": "Marketing Expert",
            "2": "Business Analyst",
            "3": "UX Designer",
            "4": "Content Strategist"
        }
        self.role_focus = {
            "Marketing Expert": "audience demographics, brand messaging, conversion potential, and market positioning",
            "Business Analyst": "business model, value proposition, competitive advantages, and market opportunities",
            "UX Designer": "usability, accessibility, user flow, visual hierarchy, and overall user experience",
            "Content Strategist": "content quality, SEO effectiveness, engagement potential, and content structure"
        }

    def get_website_content(self, url: str) -> str:
        """Load and return the content of a webpage."""
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            return docs[0].page_content
        except Exception as e:
            raise Exception(f"Error loading website content: {str(e)}")

    def get_analysis_prompt(self, role: str, content: str) -> ChatPromptTemplate:
        """Create a role-specific analysis prompt."""
        role_focus = self.role_focus[role]
        
        template = """You are an experienced {role} with 10+ years in the industry. 
        Analyze this website content and provide your professional assessment.
        
        Focus on: {role_focus}
        
        Website Content:
        {content}
        
        Provide your analysis in the following JSON format:
        {{
            "main_topic": "Brief description of the main topic or purpose of the website",
            "target_audience": "Description of the primary target audience",
            "key_insights": [
                "First key insight",
                "Second key insight",
                "Third key insight"
            ],
            "professional_recommendation": "Actionable recommendations for improvement",
            "quality_score": 0
        }}
        
        Important:
        - Quality score should be between 1-10 (10 being the best)
        - Be specific and provide concrete examples from the content
        - Use professional terminology relevant to {role}"""

        return ChatPromptTemplate.from_messages([
            ("system", template)
        ]).format_messages(role=role, role_focus=role_focus, content=content)

    def analyze_website(self, url: str, role: str) -> Dict:
        """Analyze website content from a specific professional perspective."""
        try:
            content = self.get_website_content(url)
            prompt = self.get_analysis_prompt(role, content)
            
            # Parse the output as JSON
            parser = JsonOutputParser()
            chain = self.llm | parser
            
            # Get analysis from the model
            result = chain.invoke(prompt)
            return result
            
        except Exception as e:
            return {"error": str(e)}

def get_user_choice(choices: Dict[str, str]) -> str:
    """Get and validate user's choice from a menu."""
    while True:
        print("\nSelect an expert role:")
        for key, value in choices.items():
            print(f"{key}. {value}")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in choices:
            return choices[choice]
        print("Invalid choice. Please try again.")

def main():
    print("=== Website Analysis Tool ===\n")
    
    # Initialize analyzer
    analyzer = WebsiteAnalyzer()
    
    try:
        # Get website URL
        url = input("Enter the website URL to analyze: ").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        # Verify URL is accessible
        try:
            response = requests.head(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error: Unable to access {url}. Please check the URL and try again.")
            return
        
        # Get user's role choice
        role = get_user_choice(analyzer.roles)
        
        print(f"\nAnalyzing {url} as a {role}...")
        
        # Perform analysis
        result = analyzer.analyze_website(url, role)
        
        # Display results
        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print("\n=== Analysis Results ===\n")
            print(f"Main Topic: {result.get('main_topic', 'N/A')}")
            print(f"Target Audience: {result.get('target_audience', 'N/A')}")
            
            print("\nKey Insights:")
            for i, insight in enumerate(result.get('key_insights', []), 1):
                print(f"{i}. {insight}")
            
            print(f"\nProfessional Recommendation:\n{result.get('professional_recommendation', 'N/A')}")
            print(f"\nQuality Score: {result.get('quality_score', 'N/A')}/10")
            
            # Save results to JSON file
            output_file = "website_analysis.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            print(f"\nAnalysis saved to {output_file}")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
