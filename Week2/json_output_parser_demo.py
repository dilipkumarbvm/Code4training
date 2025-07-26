# https://python.langchain.com/docs/how_to/output_parser_json/
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("⚠️  Warning: OPENAI_API_KEY not found in environment variables")
    print("Please set your OpenAI API key in a .env file or environment variable")
    exit(1)

# Define your desired data structure using Pydantic
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

def demo_json_parser_with_pydantic():
    """Demonstrate JsonOutputParser with Pydantic model for structured output"""
    print("\n📋 1. JSON PARSER WITH PYDANTIC MODEL")
    print("-" * 50)
    
    # Set up the model
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    
    # Set up a parser with the Pydantic model
    parser = JsonOutputParser(pydantic_object=Joke)

    # Get format instructions
    format_instructions = parser.get_format_instructions()
    print(format_instructions)
    
    # Create prompt with format instructions
    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    # Create the chain
    chain = prompt | model | parser
    
    print("Asking AI to tell a joke in JSON format...")
    
    # Generate structured joke
    result = chain.invoke({"query": "Tell me a joke about programming."})
    
    print(f"Result type: {type(result)}")
    print(f"Setup: {result['setup']}")
    print(f"Punchline: {result['punchline']}")
    print(f"Full result: {result}")

def demo_format_instructions():
    """Show what format instructions look like"""
    print("\n📋 2. FORMAT INSTRUCTIONS EXPLAINED")
    print("-" * 50)
    
    # Create parser for Joke
    parser = JsonOutputParser(pydantic_object=Joke)
    
    print("The parser automatically generates these instructions:")
    print("=" * 30)
    instructions = parser.get_format_instructions()
    print(instructions)
    print("=" * 30)
    print("These instructions tell the AI exactly how to format its response!")

def demo_streaming_json():
    """Demonstrate streaming capabilities of JsonOutputParser"""
    print("\n📋 3. STREAMING JSON OUTPUT")
    print("-" * 50)
    
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    parser = JsonOutputParser(pydantic_object=Joke)
    
    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    chain = prompt | model | parser
    
    print("Streaming a joke (watch it build up piece by piece):")
    print("-" * 30)
    
    # Stream the response to see partial JSON objects
    for chunk in chain.stream({"query": "Tell me a joke about computers."}):
        print(chunk)

def main():
    """
    Demonstration of JsonOutputParser from LangChain
    Based on: https://python.langchain.com/docs/how_to/output_parser_json/
    """
    
    print("📋 LangChain JSON Output Parser Demo")
    print("=" * 50)
    print("Learn how to get structured JSON from AI models")
    print()
    
    try:
        # Run core demonstrations
        demo_json_parser_with_pydantic()    # Basic structured output
        demo_format_instructions()          # See what instructions look like
        demo_streaming_json()              # Watch JSON build up in real-time
        
        print("\n" + "=" * 50)
        print("✅ JSON output parser demo completed!")
        print("\n💡 What you learned:")
        print("   • JsonOutputParser creates structured JSON output")
        print("   • Pydantic models define the expected structure")
        print("   • Format instructions guide the AI's response")
        print("   • Streaming allows real-time JSON building")
        
        print("\n📖 Reference:")
        print("   https://python.langchain.com/docs/how_to/output_parser_json/")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your API key and internet connection.")

# This runs when the file is executed directly (not imported)
if __name__ == "__main__":
    main() 