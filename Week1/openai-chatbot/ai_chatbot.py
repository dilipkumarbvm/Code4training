#!/usr/bin/env python3
"""
Simple AI Chatbot
==================

A basic chatbot that sends your input to OpenAI and displays the response.
Perfect for exploring how LLMs work and experimenting with prompts.

HOW IT WORKS:
1. Loads your OpenAI API key from environment variables
2. Creates a connection to OpenAI's servers
3. Starts a simple chat loop:
   - Gets your input
   - Sends it to OpenAI's GPT-4o-mini model
   - Displays the AI's response
   - Repeats until you type 'quit'

Requirements:
- OpenAI API key (set as environment variable OPENAI_API_KEY)
- Python packages: openai, python-dotenv

Author: AI Assistant
"""

import os                    # For accessing environment variables
import sys                   # For exiting the program cleanly
from dotenv import load_dotenv    # For loading .env files
from openai import OpenAI         # OpenAI's official Python library

def main():
    """
    Main function that runs the chatbot.
    
    This function handles:
    - Loading the API key
    - Setting up the OpenAI connection
    - Running the chat loop
    """
    
    # STEP 1: Load environment variables from .env file (if it exists)
    # This allows us to store the API key securely in a .env file
    load_dotenv()
    
    # STEP 2: Get the OpenAI API key from environment variables
    # os.getenv() looks for an environment variable named 'OPENAI_API_KEY'
    api_key = os.getenv('OPENAI_API_KEY')
    
    # STEP 3: Check if we actually got an API key
    if not api_key:
        # If no API key found, show helpful error message and exit
        print("❌ Error: OpenAI API key not found!")
        print("\nPlease set your OPENAI_API_KEY environment variable:")
        print("  Windows: set OPENAI_API_KEY=your-key-here")
        print("  Mac/Linux: export OPENAI_API_KEY=your-key-here")
        print("\nOr create a .env file with: OPENAI_API_KEY=your-key-here")
        sys.exit(1)  # Exit with error code 1
    
    # STEP 4: Initialize the OpenAI client
    # This creates a connection to OpenAI's servers using your API key
    try:
        client = OpenAI(api_key=api_key)
        print("🤖 Simple AI Chatbot Ready!")
        print("Type your message and press Enter. Type 'quit' to exit.\n")
    except Exception as e:
        # If connection fails, show error and exit
        print(f"❌ Failed to connect to OpenAI: {e}")
        sys.exit(1)
    
    # STEP 5: Main chat loop - this runs forever until user quits
    while True:
        try:
            # Get user input from the keyboard
            user_input = input("👤 You: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break  # Exit the while loop
            
            # Skip empty messages
            if not user_input:
                continue  # Go back to the start of the while loop
            
            # Show that we're getting AI response
            print("🤖 AI: ", end="", flush=True)
            
            # STEP 6: Send message to OpenAI and get response
            # This is the core API call that does the actual AI magic!
            response = client.chat.completions.create(
                model="gpt-4o-mini",              # Which AI model to use
                messages=[{"role": "user", "content": user_input}],  # Your message
                max_tokens=150,                   # Limit response length (saves money)
                temperature=0.7                   # Creativity level (0=focused, 1=creative)
            )
            
            # STEP 7: Extract the AI's text response from the API response
            # The API returns a complex object, we just want the text content
            ai_response = response.choices[0].message.content
            
            # STEP 8: Display the AI's response to the user
            print(ai_response)
            print()  # Empty line for better readability
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            # Handle any other errors (network issues, API problems, etc.)
            print(f"❌ Error: {e}")
            print("Please try again or type 'quit' to exit.\n")

# This is Python's way of saying "only run main() if this file is run directly"
# (not if it's imported as a module)
if __name__ == "__main__":
    main() 