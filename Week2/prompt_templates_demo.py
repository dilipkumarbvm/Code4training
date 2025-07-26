from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
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

def demo_basic_string_template():
    """Basic string template with one variable - shows simple, direct responses"""
    print("\n🔗 1. BASIC STRING TEMPLATE")
    print("-" * 40)
    
    # The {} syntax tells LangChain where to substitute values
    template = PromptTemplate.from_template("Tell me a fact about {topic}")
    
    print(f"Template: {template.template}")
    print(f"Variables: {template.input_variables}")
    
    # Connect template to LLM to see actual response
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=50, openai_api_key=OPENAI_API_KEY)
    chain = template | model
    
    
    topic = "artificial intelligence"
    print(f"\n📝 Topic: {topic}")
    print("🤖 LLM Response:")
    
    result = chain.invoke({"topic": topic})
    print(f"   {result.content}")
    print("\n💡 Notice: Simple, direct fact - no special formatting or context")

def demo_chat_template():
    """Chat template with system and user messages - shows teacher-style responses"""
    print("\n🔗 2. CHAT TEMPLATE")
    print("-" * 40)
    
    # ChatPromptTemplate creates multiple messages with different roles
    # Each tuple is (role, message_content)
    template = ChatPromptTemplate([
        ("system", "You are a helpful teacher who explains things clearly"),  # Sets the AI's behavior/role
        ("user", "Explain {topic} in simple terms")  # The user's request with variable
    ])
    
    print(f"Variables: {template.input_variables}")
    print("Template structure:")
    print("  System: You are a helpful teacher who explains things clearly")
    print("  User: Explain {topic} in simple terms")
    
    # Connect template to LLM to see the different response style
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=80, openai_api_key=OPENAI_API_KEY)
    chain = template | model
    
    # Use same topic for comparison
    topic = "artificial intelligence"
    print(f"\n📝 Topic: {topic}")
    print("🤖 LLM Response:")
    
    result = chain.invoke({"topic": topic})
    print(f"   {result.content}")
    print("\n💡 Notice: More educational tone due to 'teacher' system message")

def demo_with_conversation_history():
    """Template that includes conversation history - shows contextual responses"""
    print("\n🔗 3. TEMPLATE WITH CONVERSATION HISTORY")
    print("-" * 40)
    
    # MessagesPlaceholder allows you to insert a list of messages
    # This is useful for maintaining conversation context
    template = ChatPromptTemplate([
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder("history"),  # This will be replaced with actual messages
        ("user", "{question}")
    ])
    
    print(f"Variables: {template.input_variables}")  # Will show both 'history' and 'question'
    
    # Create conversation history about artificial intelligence
    # This context will influence the AI's response
    history = [
        HumanMessage(content="I'm learning about technology"),
        AIMessage(content="That's great! Technology is fascinating. What aspect interests you most?"),
        HumanMessage(content="I'm particularly curious about AI applications")
    ]
    
    print("\nConversation context:")
    for i, msg in enumerate(history, 1):
        role = "User" if isinstance(msg, HumanMessage) else "AI"
        print(f"  {i}. {role}: {msg.content}")
    
    # Connect template to LLM to see contextual response
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=100, openai_api_key=OPENAI_API_KEY)
    chain = template | model
    
    # Ask about the same topic, but with conversation context
    question = "Can you tell me about artificial intelligence?"
    print(f"\n📝 New Question: {question}")
    print("🤖 LLM Response:")
    
    result = chain.invoke({
        "history": history,
        "question": question
    })
    print(f"   {result.content}")
    print("\n💡 Notice: Response references previous conversation context")

def demo_with_ai_model():
    """Complex template with detailed instructions - shows structured responses"""
    print("\n🔗 4. COMPLEX TEMPLATE WITH DETAILED INSTRUCTIONS")
    print("-" * 40)
    
    # Create a more sophisticated template with detailed instructions
    template = ChatPromptTemplate([
        ("system", """You are an expert technology consultant. When explaining topics:
        1. Start with a clear definition
        2. Provide 2-3 key applications
        3. End with future implications
        Format your response in a structured way."""),
        ("user", "Provide a comprehensive overview of {topic}")
    ])
    
    print("Template structure:")
    print("  System: Expert consultant with detailed formatting instructions")
    print("  User: Provide a comprehensive overview of {topic}")
    
    # Create the AI model
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=150, openai_api_key=OPENAI_API_KEY)
    
    # Chain the template and model together using the | operator
    chain = template | model
    
    # Use same topic for final comparison
    topic = "artificial intelligence"
    print(f"\n📝 Topic: {topic}")
    print("🤖 LLM Response:")
    
    result = chain.invoke({"topic": topic})
    print(f"   {result.content}")
    print("\n💡 Notice: Structured, comprehensive response due to detailed system instructions")

def main():
    """
    Demonstration of how different prompt templates affect LLM responses
    """
    
    print("🎯 LangChain Prompt Templates - Response Comparison Demo")
    print("=" * 58)
    print("See how different prompt styles produce different LLM responses!")
    print("All demos use the same topic: 'artificial intelligence'")
    print()
    
    # All demos now require API key - run with error handling
    try:
        demo_basic_string_template()      # Start with simplest concept
        demo_chat_template()              # Add multiple message types  
        demo_with_conversation_history()  # Add conversation memory
        demo_with_ai_model()             # Complex instructions
        
        print("\n" + "=" * 58)
        print("✅ Demo completed!")
        print("\n🎯 COMPARISON SUMMARY:")
        print("1. Basic Template        → Simple, direct fact")
        print("2. Teacher Role          → Educational explanation") 
        print("3. With Context          → References conversation history")
        print("4. Detailed Instructions → Structured, comprehensive overview")
        print("\n💡 Key Takeaway: Different prompt styles produce VERY different responses!")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {str(e)}")
        print("💡 Make sure you have:")
        print("   1. Set up your OpenAI API key in .env file")
        print("   2. Installed requirements: pip install -r requirements.txt")
        print("   3. Have internet connection")

# This runs when the file is executed directly (not imported)
if __name__ == "__main__":
    main() 