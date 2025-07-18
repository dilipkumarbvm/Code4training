# Simple OpenAI Example

This project demonstrates the most basic way to use OpenAI's API to get an AI response. It's a beginner-friendly introduction to working with OpenAI's GPT models.

## What This Project Does

The `simple_openai_example.py` script:
- Connects to OpenAI's API using an API key
- Sends a simple prompt to the GPT-4o-mini model (asking for a bedtime story about a unicorn)
- Receives and prints the AI's response

This is the foundation for understanding how to interact with large language models programmatically.

## Prerequisites

- Python 3.11 or higher
- An OpenAI API key (free tier available)

## Setup Instructions

### 1. Get an OpenAI API Key

1. Visit [https://platform.openai.com](https://platform.openai.com)
2. Sign up for an account or log in
3. Navigate to the "API Keys" section
4. Create a new API key
5. Copy the key (you'll need it in step 3)

### 2. Install Dependencies

From the `simple_openai` folder, run:

```bash
pip install -r requirements.txt
```

This installs:
- `openai` - The official OpenAI Python library
- `python-dotenv` - For managing environment variables

### 3. Configure Your API Key

**Option A: Environment File (Recommended)**
1. Copy `env_example.txt` to `.env`:
   ```bash
   cp env_example.txt .env
   ```
2. Open `.env` and add your API key:
   ```
   OPENAI_API_KEY=your-actual-api-key-here
   ```

**Option B: Direct Code Modification**
1. Open `simple_openai_example.py`
2. Replace `"Replace with your key"` with your actual API key

## How to Run the App

### Method 1: Using Python directly
```bash
python simple_openai_example.py
```

### Method 2: Using Python module syntax
```bash
python -m simple_openai_example
```

## Expected Output

The script will output a creative one-sentence bedtime story about a unicorn, something like:

```
Once upon a time, in a magical forest filled with shimmering moonbeams, a gentle unicorn named Luna helped all the woodland creatures fall asleep by singing the sweetest lullabies with her silver voice.
```

## Understanding the Code

The script demonstrates these key concepts:

1. **API Client Setup**: Creating an OpenAI client with authentication
2. **Model Selection**: Using `gpt-4o-mini` (fast and cost-effective)
3. **Message Formatting**: Structuring prompts as conversation messages
4. **Response Handling**: Extracting the AI's text response from the API response object

## Next Steps

Once you've successfully run this example:
- Try modifying the prompt to ask different questions
- Experiment with different OpenAI models
- Explore the chat completion parameters (temperature, max_tokens, etc.)

## Troubleshooting

**Error: "Invalid API Key"**
- Double-check your API key is correctly set
- Ensure there are no extra spaces or characters

**Error: "Module not found"**
- Run `pip install -r requirements.txt` to install dependencies
- Make sure you're in the correct directory

**Error: "Rate limit exceeded"**
- You may have hit OpenAI's free tier limits
- Wait a few minutes and try again

## Cost Information

- GPT-4o-mini is very cost-effective for learning
- This simple example typically costs less than $0.001 per run
- Monitor your usage on the OpenAI dashboard 