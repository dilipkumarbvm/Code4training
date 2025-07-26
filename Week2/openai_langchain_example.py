from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
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

def main():
    """
    Simple demonstration of LangChain LCEL (LangChain Expression Language)
    Shows how to chain prompt -> model using the | operator
    """
    
    print("🔗 LangChain LCEL Demonstration")
    print("=" * 40)
    
    # Step 1: Create a prompt template
    # IMPORTANT: {topic} is a placeholder variable in curly braces {}
    # The {} syntax allows dynamic content injection into prompts
    # This is key to prompt engineering - making reusable, flexible templates
    prompt = ChatPromptTemplate.from_template(
        "Give me small report about {topic}"
    )
    print("✅ Step 1: Prompt template created")
    
    # Step 2: Initialize OpenAI model 
    model = ChatOpenAI(
        model="gpt-4o-mini",  
        max_tokens=512,         
        openai_api_key=OPENAI_API_KEY 
    )
    print("✅ Step 2: OpenAI model initialized")
    
    # Step 3: Create the LCEL chain using the | operator
    # This is the core of LCEL - chaining components with |
    # model.__ror__(prompt) = pass prompt to model
    # Notice: No output parser - we'll see the raw model response
    chain = prompt | model
    print("✅ Step 3: LCEL chain created (prompt | model)")
    print("   💡 No output parser - you'll see the raw AI response object")
    print()
    
    # Get topic from user input
    topic = input("📝 Enter a topic for your report: ").strip()
    
    if not topic:
        print("❌ No topic provided. Exiting.")
        return
    
    print(f"\n🚀 Generating report about '{topic}'...")
    print(f"   💡 The prompt will become: 'Give me small report about {topic}'")
    print("-" * 40)
    
    try:
        # .invoke() method is a unified interface that triggers the execution of a chain or component and returns its result.
        # The {topic} placeholder gets replaced with the actual topic value
        result = chain.invoke({"topic": topic})
        print("Raw model response:")
        print(f"Type: {type(result)}")
        print(f"Content: {result.content}")
        print("\n✅ Report generated successfully!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    main() 