# Simple OpenAI Example
# ===================
# This is the most basic way to use OpenAI's API to get an AI response

# Import the OpenAI library - this gives us access to OpenAI's AI models
from openai import OpenAI

# Create an OpenAI client object with your API key
# This establishes a connection to OpenAI's servers
# IMPORTANT: Replace "Replace with your key" with your actual OpenAI API key
client = OpenAI(api_key="Replace with your key")

# Make a request to OpenAI's chat completion API
# This is where the AI magic happens!
response = client.chat.completions.create(
    model="gpt-4o-mini",        # Which AI model to use (this is fast and cost-effective)
    messages=[{                 # Format messages as a conversation
        "role": "user",         # "user" means this message is from a human
        "content": "Write a one-sentence bedtime story about a unicorn."  # The actual prompt/question
    }]
)

# Extract and print the AI's response
# The API returns a complex object, so we navigate to the actual text content
print(response.choices[0].message.content) 