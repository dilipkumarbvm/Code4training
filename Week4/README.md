# Week 4: Advanced LangChain - LangGraph and Memory Management

This week focuses on building advanced conversational agents using LangGraph and implementing sophisticated memory management in LangChain v0.3. We'll explore how to create stateful agents that can maintain context across conversations and learn to implement both short-term and long-term memory solutions.

## Setup

1. **Install Required Packages**

```bash
pip install python-dotenv langgraph>=0.6.4 langchain-openai>0.3.29
```

2. **Configure OpenAI API Key**

Copy the `env_example.txt` file to `.env` and add your OpenAI API key:

```bash
cp env_example.txt .env
```

Then edit the `.env` file and add your API key and model:
```
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4o
```

To get an API key:
1. Visit https://platform.openai.com
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy the key and paste it in your `.env` file

## Topics Covered

1. Introduction to LangGraph
   - State Management
   - Graph-based Conversation Flow
   - Message Processing
2. Building Conversational Agents
   - State Definition and Type Hints
   - Message Handling and Response Generation
   - Interactive Chat Interfaces

## Project Structure

```
Week4/
├── notebooks/
│   ├── basic_langgraph.ipynb      # Basic LangGraph implementation
│   └── [other notebooks...]
├── env_example.txt
└── README.md
```

## Notebooks

### basic_langgraph.ipynb

This notebook demonstrates how to build a basic conversational agent using LangGraph. It covers:

1. **Environment Setup**
   - Package installation and imports
   - Environment variable configuration (OPENAI_API_KEY, OPENAI_MODEL)
   - API key validation

2. **State Management**
   - Defining conversation state using TypedDict
   - Message history tracking with Annotated types
   - State updates and transitions using add_messages

3. **Graph Construction**
   - Creating a StateGraph with defined State type
   - Adding nodes (chatbot function)
   - Setting up edges (START → chatbot → END)
   - Compiling the graph

4. **LLM Integration**
   - Initializing OpenAI's GPT model
   - Processing messages through the graph
   - Generating and managing responses

5. **Message Flow Implementation**
   - Handling user inputs
   - Maintaining conversation history
   - Processing responses
   - Managing state updates

6. **Interactive Interface**
   - IPython widgets for input
   - Real-time chat display
   - Conversation history visualization

Key Components:
```python
# State Definition
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Chatbot Function
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Graph Setup
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
```

## Exercises

1. **Basic Memory Implementation**
   - Create a simple conversational agent with short-term memory
   - Implement message history tracking
   - Test context retention

2. **Persistent Storage**
   - Implement SQLite-based persistent storage
   - Create a system for managing multiple conversation threads
   - Test memory persistence across sessions

3. **Advanced Agent Development**
   - Build a sophisticated agent with both short and long-term memory
   - Implement memory optimization strategies
   - Add summarization capabilities

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [LangGraph GitHub Repository](https://github.com/langchain-ai/langgraph)
- [LangGraph Documentation](https://python.langchain.com/docs/langgraph)

## Important Notes

1. Never store sensitive information or API keys directly in your code
2. Always use environment variables or secure configuration management
3. Keep your API key confidential and never commit it to version control
4. Monitor your API usage to manage costs
5. Remember to maintain conversation history for context
6. Handle message state updates properly to ensure coherent conversations