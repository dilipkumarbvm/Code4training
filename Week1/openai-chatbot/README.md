# AI Chatbot

An interactive AI chatbot application that allows you to have ongoing conversations with OpenAI's GPT models. This project demonstrates how to build a complete conversational AI interface with proper error handling and user experience features.

## What This Project Does

The `ai_chatbot.py` script creates a fully interactive chatbot that:
- Loads your OpenAI API key securely from environment variables
- Establishes a persistent connection to OpenAI's API
- Runs an interactive chat loop where you can have ongoing conversations
- Handles errors gracefully (missing API keys, network issues, etc.)
- Provides a user-friendly interface with emojis and clear prompts
- Allows you to exit cleanly by typing 'quit', 'exit', or 'bye'

This is a step up from basic API calls - it's a complete, usable chatbot application.

## Features

✅ **Interactive Conversation**: Have back-and-forth conversations with AI  
✅ **Secure API Key Management**: Uses environment variables for security  
✅ **Error Handling**: Graceful handling of network issues and API errors  
✅ **User-Friendly Interface**: Clear prompts and emojis for better UX  
✅ **Controlled Responses**: Limited token usage to manage costs  
✅ **Easy Exit**: Multiple ways to quit the conversation  
✅ **Extensive Documentation**: Every line explained with comments  

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (free tier available)
- Basic familiarity with command line/terminal

## Setup Instructions

### 1. Get an OpenAI API Key

1. Visit [https://platform.openai.com](https://platform.openai.com)
2. Sign up for an account or log in
3. Navigate to the "API Keys" section
4. Create a new API key
5. Copy the key (you'll need it in step 3)

### 2. Install Dependencies

From the `openai-chatbot` folder, run:

```bash
pip install -r requirements.txt
```

This installs:
- `openai>=1.97.0` - The official OpenAI Python library
- `python-dotenv>=1.1.1` - For secure environment variable management

### 3. Configure Your API Key

**Recommended Method: Environment File**

1. Copy the example environment file:
   ```bash
   cp env_example.txt .env
   ```

2. Open `.env` in a text editor and add your API key:
   ```
   OPENAI_API_KEY=your-actual-api-key-here
   ```

**Alternative Method: System Environment Variable**

**Windows:**
```cmd
set OPENAI_API_KEY=your-actual-api-key-here
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY=your-actual-api-key-here
```

## How to Run the Chatbot

### Method 1: Direct Python execution
```bash
python ai_chatbot.py
```

### Method 2: Python module syntax
```bash
python -m ai_chatbot
```

## How to Use the Chatbot

1. **Start the Application**: Run the command above
2. **Wait for Ready Message**: You'll see "🤖 Simple AI Chatbot Ready!"
3. **Start Chatting**: Type your message and press Enter
4. **Continue Conversation**: The AI will respond, then you can reply
5. **Exit**: Type 'quit', 'exit', or 'bye' to end the conversation

### Example Conversation

```
🤖 Simple AI Chatbot Ready!
Type your message and press Enter. Type 'quit' to exit.

👤 You: Hello! What's the weather like today?
🤖 AI: Hello! I don't have access to real-time weather data, but I'd be happy to help you find weather information! You could check a weather app, website like weather.com, or ask a voice assistant for current conditions in your area.

👤 You: Can you help me write a poem about coding?
🤖 AI: Absolutely! Here's a short poem about coding:

Lines of logic, loops that flow,
Variables dancing to and fro,
Debug the errors, fix each flaw,
Code is art without a flaw.

👤 You: quit
👋 Goodbye!
```

## Understanding the Code

This project demonstrates several important programming concepts:

### 1. **Environment Variable Management**
- Secure API key storage using `.env` files
- Fallback to system environment variables
- Error handling for missing configuration

### 2. **API Integration**
- Connecting to external APIs (OpenAI)
- Handling API responses and errors
- Managing API parameters (model, tokens, temperature)

### 3. **User Interface Design**
- Interactive command-line interface
- User feedback with emojis and clear prompts
- Graceful exit handling

### 4. **Error Handling**
- Network error recovery
- Missing configuration detection
- Keyboard interrupt handling (Ctrl+C)

### 5. **Program Structure**
- Main function organization
- Infinite loop with break conditions
- Clean code with extensive documentation

## Configuration Options

The chatbot uses these default settings:

- **Model**: `gpt-4o-mini` (fast and cost-effective)
- **Max Tokens**: 150 (limits response length)
- **Temperature**: 0.7 (balanced creativity)

You can modify these in the code to experiment with different behaviors.

## Troubleshooting

### "❌ Error: OpenAI API key not found!"
- **Solution**: Make sure your `.env` file exists and contains your API key
- **Check**: Ensure there are no extra spaces around your API key
- **Verify**: Your API key should start with `sk-`

### "❌ Failed to connect to OpenAI"
- **Solution**: Check your internet connection
- **Verify**: Your API key is valid and has credit available
- **Try**: Wait a moment and run the script again

### "Module not found" errors
- **Solution**: Run `pip install -r requirements.txt`
- **Check**: You're in the correct `openai-chatbot` directory
- **Try**: Use `pip3` instead of `pip` if on Mac/Linux

### Rate limit errors
- **Solution**: Wait a few minutes before trying again
- **Info**: Free tier has usage limits
- **Monitor**: Check your usage on OpenAI's dashboard

## Cost Management

- **Token Limit**: Responses are limited to 150 tokens to control costs
- **Model Choice**: GPT-4o-mini is the most cost-effective option
- **Typical Cost**: Each conversation turn costs approximately $0.001-0.002
- **Monitoring**: Check your usage on the OpenAI platform dashboard

## Next Steps

Once you've successfully run the chatbot, you can experiment with the basic settings in the code such as adjusting the temperature or trying different models.


## Learning Objectives

This project teaches:
- **API Integration**: How to work with external AI services
- **Environment Management**: Secure configuration handling
- **User Experience**: Creating intuitive command-line interfaces
- **Error Handling**: Building robust applications
- **Code Organization**: Structuring larger Python programs

Perfect for understanding how modern AI applications are built! 