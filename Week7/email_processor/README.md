# Enhanced Email Processing MCP Server

An advanced Model Context Protocol (MCP) server for processing and managing email threads with sophisticated analysis and response generation.

## Features

- Complete email thread analysis
- Multilingual support
- Sentiment analysis
- Action item extraction
- Similar case finding
- Priority management
- Department routing
- Persistent storage

## Setup for Windows

1. Create and activate virtual environment:
```powershell
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Create `.env` file:
   - Create a new file named `.env` in the email_processor directory
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   - Replace 'your_openai_api_key_here' with your actual OpenAI API key
   - Save the file

   Note: The .env file can be placed in:
   - The email_processor directory
   - The parent directory
   - Your home directory

## Testing with MCP Inspector

1. Start the server:
```powershell
python email_processor.py
```

[Rest of the README remains the same...]