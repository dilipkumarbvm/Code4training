# 🚀 Week 4 LangGraph Exercise - Multi-Role Assistant

**Build conversational agents using LangGraph's state management and graph-based flows**

## 🎯 Learning Approach

These exercises focus on building a multi-role assistant using LangGraph, with both basic and advanced implementations. Start with the basic version to understand core concepts, then progress to the advanced version for more sophisticated features.

**Your Mission**: Complete both versions to understand LangGraph's capabilities!

---

## 📋 Prerequisites

✅ **Complete the basic_langgraph.ipynb** tutorial  
✅ **API Key Setup** - Your `.env` file with:
```
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4
```
✅ **Dependencies** - Install required packages:
```bash
pip install python-dotenv langgraph>=0.6.4 langchain-openai>0.3.29
```

---

## 🤖 Basic Exercise 1: Simple Multi-Role Assistant
**Focus: Core LangGraph Concepts**

### 🎯 What You'll Build
A simple conversational agent that can switch between two roles: Technical Helper and Creative Helper.

### 📝 Your Task
Create `basic_role_assistant.py` that implements:

1. **Basic Roles (2 personas):**
   - Technical Helper
     - Programming help
     - Technical explanations
   - Creative Helper
     - Writing help
     - Creative ideas

2. **Simple State Management:**
```python
class State(TypedDict):
    """Basic state structure"""
    messages: Annotated[list, add_messages]  # Conversation history
    current_role: str  # Active role
```

3. **Core Functions:**
```python
def initialize_state() -> State:
    """Create initial state"""
    return {
        "messages": [],
        "current_role": "technical"  # Default role
    }

def process_role_switch(state: State) -> dict:
    """Basic role switch detection"""
    last_message = state["messages"][-1].content.lower()
    
    # Simple role switching
    if "switch to technical" in last_message:
        return {"messages": state["messages"], "current_role": "technical"}
    elif "switch to creative" in last_message:
        return {"messages": state["messages"], "current_role": "creative"}
    
    return {"messages": state["messages"]}

def generate_response(state: State) -> dict:
    """Generate basic role-based response"""
    role = state["current_role"]
    
    # Simple role-based prompting
    if role == "technical":
        prompt = "You are a technical expert. Help with technical questions."
    else:
        prompt = "You are a creative helper. Assist with creative tasks."
    
    response = llm.invoke(
        state["messages"],
        system_prompt=prompt
    )
    
    return {"messages": [response]}
```

4. **Basic Graph Structure:**
```python
# Create simple graph
graph = (
    StateGraph(State)
    .add_node("role_switch", process_role_switch)
    .add_node("response", generate_response)
    .set_entry_point("role_switch")
    .add_edge("role_switch", "response")
    .add_edge("response", END)
    .compile()
)
```

5. **Simple Interface:**
```python
def create_basic_interface():
    """Create simple chat interface"""
    text_input = widgets.Text(
        description='Message:',
        placeholder='Type your message...'
    )
    send_button = widgets.Button(description='Send')
    output = widgets.Output()
    
    return text_input, send_button, output
```

### 🧪 Test Cases
```python
# Test basic role switching
messages = [
    HumanMessage(content="Help me with Python"),
    HumanMessage(content="switch to creative"),
    HumanMessage(content="Help me write a poem")
]
```

### 🎯 Success Criteria
- [ ] Basic role switching works
- [ ] Appropriate responses per role
- [ ] Simple conversation flow
- [ ] Basic error handling

---

## 🤖 Basic Exercise 2: Two-Node Processor
**Focus: Understanding Node Communication**

### 🎯 What You'll Build
A graph with two processing nodes that work together to enhance messages:
1. First node analyzes and adds context
2. Second node generates an enhanced response

### 📝 Your Task
Create `two_node_processor.py` that implements:

1. **Enhanced State Structure:**
```python
class State(TypedDict):
    """State with analysis and messages"""
    messages: Annotated[list, add_messages]  # Conversation history
    analysis: dict  # Message analysis results
```

2. **Node Functions:**
```python
def analyze_message(state: State) -> dict:
    """First node: Analyze message and add context"""
    last_message = state["messages"][-1].content
    
    # Simple analysis
    analysis = {
        "length": len(last_message),
        "question": "?" in last_message,
        "topics": extract_key_topics(last_message),
        "sentiment": analyze_sentiment(last_message)
    }
    
    return {
        "messages": state["messages"],
        "analysis": analysis
    }

def generate_enhanced_response(state: State) -> dict:
    """Second node: Use analysis to generate better response"""
    analysis = state["analysis"]
    
    # Create enhanced prompt based on analysis
    system_prompt = f"""
    Message analysis:
    - Length: {analysis['length']} characters
    - Type: {'Question' if analysis['question'] else 'Statement'}
    - Topics: {', '.join(analysis['topics'])}
    - Sentiment: {analysis['sentiment']}
    
    Provide a detailed response addressing these aspects.
    """
    
    response = llm.invoke(
        state["messages"],
        system_prompt=system_prompt
    )
    
    return {"messages": [response]}
```

3. **Helper Functions:**
```python
def extract_key_topics(text: str) -> list:
    """Extract main topics from text"""
    # Simple keyword extraction
    common_topics = ["python", "code", "data", "help", "how", "what"]
    return [word for word in text.lower().split() 
            if word in common_topics]

def analyze_sentiment(text: str) -> str:
    """Basic sentiment analysis"""
    positive = ["good", "great", "help", "please", "thanks"]
    negative = ["bad", "error", "wrong", "issue", "problem"]
    
    pos_count = sum(1 for word in text.lower().split() 
                   if word in positive)
    neg_count = sum(1 for word in text.lower().split() 
                   if word in negative)
    
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    return "neutral"
```

4. **Two-Node Graph Structure:**
```python
# Create graph with two processing nodes
graph = (
    StateGraph(State)
    .add_node("analyzer", analyze_message)
    .add_node("responder", generate_enhanced_response)
    .set_entry_point("analyzer")
    .add_edge("analyzer", "responder")
    .add_edge("responder", END)
    .compile()
)
```

5. **Testing Interface:**
```python
def test_processor(message: str):
    """Test the two-node processor"""
    # Initialize state
    initial_state = {
        "messages": [HumanMessage(content=message)],
        "analysis": {}
    }
    
    # Process through graph
    result = graph.invoke(initial_state)
    
    # Show results
    print("Input Message:", message)
    print("\nAnalysis:", result["analysis"])
    print("\nResponse:", result["messages"][-1].content)
```

### 🧪 Test Cases
```python
# Test different message types
test_messages = [
    "Can you help me understand Python functions?",
    "This code keeps giving me errors!",
    "Thanks for explaining that so well.",
    "What's the best way to analyze data in Python?"
]

for msg in test_messages:
    test_processor(msg)
    print("\n" + "="*50 + "\n")
```

### 🎯 Success Criteria
- [ ] Message analysis works correctly
- [ ] Analysis affects final response
- [ ] Graph properly chains both nodes
- [ ] Different message types get appropriate responses
- [ ] Basic error handling in both nodes

### 💡 Learning Points
1. How nodes communicate through state
2. How to chain processing steps
3. How to enhance responses with context
4. Basic message analysis techniques

---

[Rest of the file remains unchanged...]