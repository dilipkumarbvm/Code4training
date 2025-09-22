#!/usr/bin/env python3
"""
Simple AI Chatbot (Anthropic / Claude)
======================================

A basic chatbot that sends your input to Anthropic Claude and displays the response.

HOW IT WORKS:
1. Loads your Anthropic API key from environment variables
2. Creates a connection to Anthropic
3. Starts a simple chat loop:
   - Gets your input
   - Sends it to Claude (e.g., claude-3-haiku-20240307)
   - Displays the AI's response
   - Repeats until you type 'quit'

Requirements:
- Anthropic API key (set as environment variable ANTHROPIC_API_KEY)
- Python packages: anthropic, python-dotenv

Author: AI Assistant
"""

import os
import sys
from dotenv import load_dotenv
from anthropic import Anthropic

def main():
    """
    Main function that runs the chatbot with Anthropic Claude.
    """

    # STEP 1: Load environment variables from .env file (if it exists)
    load_dotenv()

    # STEP 2: Get the Anthropic API key from environment variables
    api_key = os.getenv('ANTHROPIC_API_KEY')

    # STEP 3: Check if we actually got an API key
    if not api_key:
        print("❌ Error: Anthropic API key not found!")
        print("\nPlease set your ANTHROPIC_API_KEY environment variable:")
        print("  Windows: set ANTHROPIC_API_KEY=your-key-here")
        print("  Mac/Linux: export ANTHROPIC_API_KEY=your-key-here")
        print("\nOr create a .env file with: ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)

    # STEP 4: Initialize the Anthropic client
    try:
        client = Anthropic(api_key=api_key)  # reads from env if not passed explicitly
        print("🤖 Simple Claude Chatbot Ready!")
        print("Type your message and press Enter. Type 'quit' to exit.\n")
    except Exception as e:
        print(f"❌ Failed to connect to Anthropic: {e}")
        sys.exit(1)

    # STEP 5: Main chat loop
    while True:
        try:
            user_input = input("👤 You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break

            if not user_input:
                continue

            print("🤖 AI: ", end="", flush=True)

            # STEP 6: Send message to Anthropic Claude and get response
            response = client.messages.create(
                model="claude-3-haiku-20240307",   # or claude-3.5-sonnet, claude-3-opus, etc.
                max_tokens=150,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            # STEP 7: Extract the AI's text response (Anthropic format)
            # response.content is a list of content blocks; grab text blocks
            ai_response = "".join(
                block.text for block in response.content
                if getattr(block, "type", None) == "text"
            ) or "[No text content returned]"

            # STEP 8: Display the AI's response
            print(ai_response)
            print()

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.\n")

if __name__ == "__main__":
    main()
