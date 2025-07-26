# https://python.langchain.com/docs/integrations/document_loaders/web_base/
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
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

def demo_basic_webpage_loading():
    """Load content from a single webpage"""
    print("\n🌐 1. BASIC WEBPAGE LOADING")
    print("-" * 40)
    
    # Create a loader for a specific webpage
    # WebBaseLoader implements the BaseLoader interface
    loader = WebBaseLoader("https://python.langchain.com/docs/concepts/document_loaders/")
    
    print("Loading webpage content...")
    
    # Use the .load() method to get all documents at once
    # This returns a list of Document objects
    documents = loader.load()
    
    print(f"Number of documents loaded: {len(documents)}")
    print(f"Document type: {type(documents[0])}")
    
    # Each document has content and metadata
    first_doc = documents[0]
    print(f"Content length: {len(first_doc.page_content)} characters")
    print(f"Source URL: {first_doc.metadata.get('source', 'Unknown')}")
    
    # Show a preview of the content
    preview = first_doc.page_content[:300] + "..." if len(first_doc.page_content) > 300 else first_doc.page_content
    print(f"\nContent preview:\n{preview}")

def demo_webpage_with_ai():
    """Use loaded webpage content with AI for summarization"""
    print("\n🌐 2. WEBPAGE CONTENT WITH AI")
    print("-" * 40)
    
    # Load webpage content
    loader = WebBaseLoader("https://python.langchain.com/docs/concepts/document_loaders/")
    documents = loader.load()
    
    if not documents:
        print("No documents loaded!")
        return
    
    # Get the content from the first document
    webpage_content = documents[0].page_content
    
    # Create a simple prompt template for summarization
    template = ChatPromptTemplate([
        ("system", "You are a helpful assistant that summarizes web content clearly"),
        ("user", "Please provide a brief summary of this webpage:\n\n{content}")
    ])
    
    # Set up the AI model and chain
    model = ChatOpenAI(model="gpt-4o-mini", max_tokens=150, openai_api_key=OPENAI_API_KEY)
    parser = StrOutputParser()
    
    # Create the chain: template → model → parser
    chain = template | model | parser
    
    print("Creating AI summary of the webpage...")
    
    # Truncate content if too long (to stay within token limits)
    max_content_length = 2000
    if len(webpage_content) > max_content_length:
        webpage_content = webpage_content[:max_content_length] + "..."
        print("(Content truncated to fit token limits)")
    
    # Generate summary using the chain
    try:
        summary = chain.invoke({"content": webpage_content})
        
        print(f"\n📄 AI Summary:")
        print(summary)
        
    except Exception as e:
        print(f"❌ Error generating summary: {str(e)}")
        print("Please check your API key and internet connection.")

def main():
    """
    Simple demonstration of LangChain Document Loaders for Webpages
    """
    
    print("🌐 LangChain Webpage Loader - Simple Demo")
    print("=" * 50)
    print("Learn how to load and process web content")
    print()
    
    try:
        # Run the two core demonstrations
        demo_basic_webpage_loading()    # Load webpage content
        demo_webpage_with_ai()         # Process content with AI
        
        print("\n" + "=" * 50)
        print("✅ Webpage loader demo completed!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your internet connection.")

# This runs when the file is executed directly (not imported)
if __name__ == "__main__":
    main() 