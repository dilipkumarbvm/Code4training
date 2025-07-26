from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

# Customer support email that needs classification
CUSTOMER_EMAIL = """
Subject: Order #12345 - Wrong Item Received

Hi there,

I ordered a blue sweater (size M) last week but received a red jacket (size L) instead. 
This is really frustrating because I needed it for an event tomorrow. 

Can you please help me get the right item or process a refund quickly?

Best regards,
Sarah Johnson
"""

def demo_zero_shot_prompting():
    """
    Zero-shot prompting: Ask the AI to perform a task without any examples
    - Simple and direct
    - Relies on the AI's pre-trained knowledge
    - Good for straightforward tasks
    """
    print("\n🎯 1. ZERO-SHOT PROMPTING")
    print("-" * 50)
    print("Definition: Ask AI to do something without providing examples")
    print()
    
    # Create a simple, direct prompt with no examples
    prompt = ChatPromptTemplate([
        ("user", "Classify this customer email into one of these categories: "
                  "Complaint, Question, Refund Request, or Compliment.\n\n"
                  "Email: {email}")
    ])
    
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = prompt | model | StrOutputParser()
    
    print("📧 Customer Email:")
    print(CUSTOMER_EMAIL)
    print("\n🤖 AI Response (Zero-shot):")
    
    result = chain.invoke({"email": CUSTOMER_EMAIL})
    print(result)

def demo_few_shot_prompting():
    """
    Few-shot prompting: Provide examples before asking the AI to perform the task
    - Shows the AI the expected format and reasoning
    - More consistent results
    - Good when you want specific formatting or approach
    """
    print("\n🎯 2. FEW-SHOT PROMPTING")
    print("-" * 50)
    print("Definition: Provide examples to show the AI how to respond")
    print()
    
    # Create examples of email classifications
    examples = [
        {
            "email": "Subject: Great Service!\nYour team was amazing. Fast delivery and perfect product!",
            "classification": "Compliment - Customer expressing satisfaction with service and product"
        },
        {
            "email": "Subject: Question about shipping\nHow long does international shipping usually take?",
            "classification": "Question - Customer asking for information about shipping times"
        },
        {
            "email": "Subject: Return my purchase\nI want to return this item and get my money back.",
            "classification": "Refund Request - Customer wants to return product and get refund"
        }
    ]
    
    # Create few-shot prompt template
    example_prompt = ChatPromptTemplate([
        ("user", "Email: {email}"),
        ("assistant", "Classification: {classification}")
    ])
    
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
    )
    
    final_prompt = ChatPromptTemplate([
        few_shot_prompt,
        ("user", "Email: {email}")
    ])
    
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = final_prompt | model | StrOutputParser()
    
    print("📚 Examples provided to AI:")
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example['email'][:50]}... → {example['classification']}")
    
    print("\n📧 New Customer Email:")
    print(CUSTOMER_EMAIL[:100] + "...")
    print("\n🤖 AI Response (Few-shot):")
    
    result = chain.invoke({"email": CUSTOMER_EMAIL})
    print(result)

def demo_chain_of_thought():
    """
    Chain-of-Thought (CoT) prompting: Ask the AI to show its reasoning step by step
    - More transparent decision-making
    - Better for complex problems
    - Helps verify the AI's logic
    """
    print("\n🎯 3. CHAIN-OF-THOUGHT (CoT) PROMPTING")
    print("-" * 50)
    print("Definition: Ask AI to explain its reasoning step by step")
    print()
    
    # Prompt that asks for step-by-step reasoning
    prompt = ChatPromptTemplate([
        ("user", "Classify this customer email into one of these categories: "
                  "Complaint, Question, Refund Request, or Compliment.\n\n"
                  "Think step by step:\n"
                  "1. First, identify the main issue or request\n"
                  "2. Look for emotional tone (frustrated, happy, neutral)\n"
                  "3. Determine what action the customer wants\n"
                  "4. Choose the most appropriate category\n"
                  "5. Explain your reasoning\n\n"
                  "Email: {email}")
    ])
    
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = prompt | model | StrOutputParser()
    
    print("📧 Customer Email:")
    print(CUSTOMER_EMAIL[:100] + "...")
    print("\n🤖 AI Response (Chain-of-Thought):")
    
    result = chain.invoke({"email": CUSTOMER_EMAIL})
    print(result)

def demo_role_prompting():
    """
    Role prompting: Ask the AI to act as a specific persona or expert
    - Leverages domain expertise
    - More contextually appropriate responses
    - Better understanding of nuances
    """
    print("\n🎯 4. ROLE PROMPTING")
    print("-" * 50)
    print("Definition: Ask AI to act as a specific expert or persona")
    print()
    
    # Prompt that assigns a specific role to the AI
    prompt = ChatPromptTemplate([
        ("system", "You are an experienced customer service manager with 10 years of experience "
                   "handling customer emails. You understand customer emotions and business priorities. "
                   "You're known for your ability to quickly assess situations and provide helpful guidance."),
        ("user", "As a customer service manager, classify this email and provide guidance on "
                  "how urgent this case is and what action should be taken.\n\n"
                  "Categories: Complaint, Question, Refund Request, or Compliment\n"
                  "Urgency: Low, Medium, High\n"
                  "Action: What should the support team do?\n\n"
                  "Email: {email}")
    ])
    
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = prompt | model | StrOutputParser()
    
    print("👤 AI Role: Experienced Customer Service Manager")
    print("\n📧 Customer Email:")
    print(CUSTOMER_EMAIL[:100] + "...")
    print("\n🤖 AI Response (Role-based):")
    
    result = chain.invoke({"email": CUSTOMER_EMAIL})
    print(result)

def demo_comparison():
    """
    Show a quick comparison of all techniques
    """
    print("\n🎯 5. TECHNIQUE COMPARISON")
    print("-" * 50)
    print("Summary of when to use each technique:")
    print()
    print("✅ Zero-shot:")
    print("   • Simple, direct tasks")
    print("   • When you trust the AI's built-in knowledge")
    print("   • Quick and efficient")
    print()
    print("✅ Few-shot:")
    print("   • When you want consistent formatting")
    print("   • Complex tasks that benefit from examples")
    print("   • When you need specific output style")
    print()
    print("✅ Chain-of-Thought:")
    print("   • Complex reasoning or problem-solving")
    print("   • When you need to verify AI's logic")
    print("   • Math problems, analysis tasks")
    print()
    print("✅ Role Prompting:")
    print("   • Domain-specific expertise needed")
    print("   • When context and perspective matter")
    print("   • Professional or specialized tasks")

def main():
    """
    Demonstration of key prompting techniques using customer support as real-world example
    """
    
    print("🎯 Prompting Techniques Demo")
    print("=" * 50)
    print("Real-world example: Customer support email classification")
    print()
    
    try:
        # Demonstrate each technique with the same email
        demo_zero_shot_prompting()      # Direct, no examples
        demo_few_shot_prompting()       # With examples
        demo_chain_of_thought()         # Step-by-step reasoning
        demo_role_prompting()           # Expert persona
        demo_comparison()               # When to use each
        
        print("\n" + "=" * 50)
        print("✅ Prompting techniques demo completed!")
        print("\n💡 Key Takeaway:")
        print("   Different prompting techniques can dramatically change")
        print("   the quality and style of AI responses!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your API key and internet connection.")

# This runs when the file is executed directly (not imported)
if __name__ == "__main__":
    main() 