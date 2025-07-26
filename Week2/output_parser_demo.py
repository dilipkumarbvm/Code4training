from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
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

def demo_with_string_parser():
    """Demonstrate LCEL chain WITH StrOutputParser"""
    print("\n🔗 WITH STRING OUTPUT PARSER:")
    print("-" * 40)
    
    prompt = ChatPromptTemplate.from_template("Write a short poem about {topic}")
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=200, openai_api_key=OPENAI_API_KEY)
    string_parser = StrOutputParser()
    
    # Chain WITH parser
    chain = prompt | model | string_parser
    
    result = chain.invoke({"topic": "coding"})
    print(f"Output type: {type(result)}")
    print(f"Content:\n{result}")

def demo_without_parser():
    """Demonstrate LCEL chain WITHOUT any output parser"""
    print("\n🔗 WITHOUT OUTPUT PARSER:")
    print("-" * 40)
    
    prompt = ChatPromptTemplate.from_template("Write a short poem about {topic}")
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=200, openai_api_key=OPENAI_API_KEY)
    
    # Chain WITHOUT parser
    chain = prompt | model
    
    result = chain.invoke({"topic": "coding"})
    print(f"Output type: {type(result)}")
    print(f"Content: {result.content}")
    print(f"Additional attributes available: {[attr for attr in dir(result) if not attr.startswith('_')][:5]}...")

def main():
    """
    Demonstration of StrOutputParser in LangChain
    Shows the difference between using and not using an output parser
    """
    
    print("🎯 LangChain StrOutputParser Demonstration")
    print("=" * 60)
    
    print()
    
    try:
        # Show both approaches for comparison
        demo_without_parser()
        demo_with_string_parser()
        
        print("\n" + "=" * 60)
        print("✅ StrOutputParser demonstration completed!")

        
        print("\n📝 Next Steps:")
        print("   Check TODO_week2.md for exercises with other output parsers!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    main() 