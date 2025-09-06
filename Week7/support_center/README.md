# Support Center MCP Server

This is a Model Context Protocol (MCP) server implementation for handling customer support tickets using OpenAI's GPT-4.

## Features

- Create and manage support tickets
- Automated ticket analysis (sentiment, urgency, category)
- Intelligent response generation
- Conversation history tracking

## Setup for Windows

1. Create and navigate to project directory:
```powershell
mkdir support_center
cd support_center
```

2. Create and activate virtual environment:
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

3. Install Python dependencies:
```powershell
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Testing with MCP Inspector

The MCP Inspector is a powerful tool for testing and debugging your MCP server. Here's how to set it up:

1. Install Node.js and npm:
   - Download from [Node.js website](https://nodejs.org/)
   - Choose the LTS (Long Term Support) version
   - Run the installer

2. Install MCP Inspector:
```powershell
npm install -g @modelcontextprotocol/inspector
```

3. Run the Inspector with your server:
```powershell
# From your project directory
npx @modelcontextprotocol/inspector python support.py
```

4. Using the Inspector Interface:
   - The Inspector will open in your default web browser
   - Navigate to the Tools tab to test your server
   - Monitor server logs in the Notifications pane

5. Testing Tools:
   - Click on a tool to expand its details
   - Fill in the required parameters
   - Click "Execute" to test the tool
   - View the response in the results panel

## Running in Production

Run the server:
```powershell
python support.py
```

## Configuration with Claude for Desktop (Windows)

1. Create/edit your Claude configuration file:
   - Location: `%APPDATA%\Claude\claude_desktop_config.json`
   - You can open this location by:
     1. Press `Win + R`
     2. Type `%APPDATA%\Claude`
     3. Press Enter

2. Add the following configuration (use forward slashes or double backslashes for paths):
```json
{
  "mcpServers": {
    "support_center": {
      "command": "python",
      "args": [
        "C:/Users/YourUsername/Path/To/Week7/support_center/support.py"
      ],
      "env": {
        "OPENAI_API_KEY": "your_openai_api_key_here",
        "PYTHONPATH": "C:/Users/YourUsername/Path/To/Week7/support_center/venv/Lib/site-packages"
      }
    }
  }
}
```

Note: Replace `C:/Users/YourUsername/Path/To` with your actual path to the project. You can get this by:
1. Open PowerShell in your project directory
2. Type `pwd` and press Enter
3. Use that path in the configuration

## Troubleshooting

1. Inspector Issues:
   - Ensure Node.js and npm are installed: `node --version` and `npm --version`
   - Try updating npm: `npm update -g @modelcontextprotocol/inspector`
   - Check if the server is running: `python support.py`
   - Try running Inspector with full Python path

2. Server Issues:
   - Double-check your paths in `claude_desktop_config.json`
   - Ensure you're using forward slashes (`/`) or double backslashes (`\\`)
   - Make sure the path is absolute, not relative
   - Verify PYTHONPATH points to your virtual environment's site-packages

3. Module Issues:
   - Make sure you activated the virtual environment
   - Try reinstalling the packages with `pip install -r requirements.txt`
   - Verify the PYTHONPATH in claude_desktop_config.json points to your venv's site-packages

## Available Tools

1. `create_ticket`: Create new support tickets
2. `add_message`: Add messages to existing tickets
3. `get_ticket_status`: Check ticket status and history

## Example Test Cases in Inspector

1. Create Ticket:
```json
{
    "customer_id": "test_customer",
    "subject": "Login Issue",
    "description": "Cannot access my account"
}
```

2. Add Message:
```json
{
    "ticket_id": 1,
    "message": "I tried resetting my password",
    "is_customer": true
}
```

3. Get Status:
```json
{
    "ticket_id": 1
}
```