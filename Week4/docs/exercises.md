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

## 🤖 Basic Exercise: Simple Multi-Role Assistant
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

## 🚀 Advanced Exercise: Sophisticated Multi-Role Assistant
**Focus: Complex State Management and Advanced Features**

### 🎯 Advanced Implementation Details

1. **Role-Specific Prompt Engineering:**
```python
def create_role_prompt(role: str, context: dict) -> str:
    """Create sophisticated role-specific prompts"""
    base_prompts = {
        "technical": """You are an expert technical advisor with deep knowledge in:
            - Programming and software development
            - System architecture and design
            - Technical problem-solving
            Current expertise focus: {expertise}
            Communication style: {style}
            """,
        "creative": """You are an experienced creative professional skilled in:
            - Creative writing and storytelling
            - Content creation and ideation
            - Artistic expression
            Current focus: {expertise}
            Expression style: {style}
            """,
        # Add other role prompts...
    }
    
    return base_prompts[role].format(**context)
```

2. **Context Management System:**
```python
def update_role_context(state: State, new_context: dict) -> State:
    """Sophisticated context management"""
    role = state["current_role"]
    
    # Deep merge existing and new context
    updated_context = {
        **state["role_context"][role],
        **new_context,
        "last_topics": extract_topics(state["messages"][-5:]),
        "key_points": summarize_discussion(state["messages"]),
        "timestamp": datetime.now().isoformat()
    }
    
    # Update state immutably
    new_role_context = {
        **state["role_context"],
        role: updated_context
    }
    
    return {
        **state,
        "role_context": new_role_context
    }
```

3. **Advanced Role Switching Logic:**
```python
def determine_new_role(message: str, current_state: State) -> tuple[str, float]:
    """Sophisticated role detection with confidence scoring"""
    # Define role patterns and keywords
    role_patterns = {
        "technical": r"(?i)(coding|programming|technical|development|debug)",
        "creative": r"(?i)(writing|story|creative|design|artistic)",
        "business": r"(?i)(analysis|strategy|market|business|metrics)",
        "life_coach": r"(?i)(advice|life|goals|personal|motivation)"
    }
    
    # Calculate confidence scores
    scores = {}
    for role, pattern in role_patterns.items():
        matches = len(re.findall(pattern, message))
        context_relevance = calculate_context_relevance(
            message, 
            current_state["role_context"][role]
        )
        scores[role] = (matches * 0.6) + (context_relevance * 0.4)
    
    # Get best match
    best_role = max(scores.items(), key=lambda x: x[1])
    return best_role
```

4. **Enhanced Response Generation:**
```python
def generate_enhanced_response(state: State) -> dict:
    """Generate contextually aware responses"""
    role = state["current_role"]
    context = state["role_context"][role]
    
    # Create enhanced prompt with context
    system_prompt = create_role_prompt(role, context)
    
    # Add context-specific instructions
    system_prompt += f"""
    Previous key points: {context.get('key_points', [])}
    Current focus: {context.get('expertise', 'general')}
    Style guide: {context.get('style', 'professional')}
    """
    
    # Generate response with role-specific formatting
    response = llm.invoke(
        state["messages"],
        system_prompt=system_prompt
    )
    
    # Format response based on role
    formatted_response = format_role_response(response, role)
    
    return {
        "messages": [formatted_response],
        "context_update": extract_new_context(response)
    }
```

5. **Advanced Error Handling:**
```python
def safe_state_update(state: State, updates: dict) -> State:
    """Safe state updating with validation"""
    try:
        # Validate updates
        if "current_role" in updates:
            assert updates["current_role"] in VALID_ROLES
        
        if "role_context" in updates:
            validate_context_structure(updates["role_context"])
        
        # Create new state immutably
        new_state = {
            **state,
            **updates,
            "last_update": datetime.now().isoformat()
        }
        
        # Validate final state
        validate_state_structure(new_state)
        return new_state
        
    except AssertionError as e:
        logger.error(f"Invalid state update: {e}")
        return state  # Return unchanged state on error
    except Exception as e:
        logger.error(f"State update error: {e}")
        return state
```

6. **Advanced Graph Configuration:**
```python
# Create sophisticated graph with error handling and context management
graph = (
    StateGraph(State)
    .add_node("validate_input", validate_user_input)
    .add_node("role_switch", process_role_switch)
    .add_node("context_update", update_role_context)
    .add_node("response", generate_enhanced_response)
    .add_node("error_handler", handle_errors)
    .set_entry_point("validate_input")
)

# Add sophisticated edge conditions
graph.add_conditional_edges(
    "validate_input",
    lambda x: "role_switch" if detect_role_switch(x) else "context_update"
)
graph.add_edge("role_switch", "context_update")
graph.add_edge("context_update", "response")
graph.add_edge("response", END)

# Add error handling edges
graph.add_edge("validate_input", "error_handler", condition=lambda x: "error" in x)
graph.add_edge("role_switch", "error_handler", condition=lambda x: "error" in x)
graph.add_edge("error_handler", END)

# Compile with validation
graph = graph.compile()
```

### 💡 Advanced Implementation Tips

1. **State Management:**
   - Use immutable state updates
   - Implement deep copying for nested structures
   - Add timestamps for state changes
   - Include validation at every step

2. **Context Handling:**
   - Implement context summarization
   - Add relevance scoring
   - Use sliding window for recent context
   - Include metadata for each context update

3. **Response Generation:**
   - Add role-specific formatting
   - Include context-aware prompting
   - Implement response validation
   - Add fallback responses

4. **Error Handling:**
   - Implement comprehensive validation
   - Add logging and monitoring
   - Create recovery mechanisms
   - Handle edge cases gracefully

5. **Performance Optimization:**
   - Implement context pruning
   - Add response caching
   - Optimize state updates
   - Monitor memory usage

---

## 📈 Comparison of Implementations

### Basic Version
- Two simple roles
- Basic state management
- Simple role switching
- Minimal interface
- No context retention

### Advanced Version
- Four detailed roles
- Complex state with context
- Sophisticated role switching
- Rich interface
- Context retention per role
- Detailed response formatting
- Advanced error handling

## 🔄 Learning Path

1. **Start with Basic Version:**
   - Understand state management
   - Implement simple role switching
   - Create basic conversation flow

2. **Progress to Advanced Version:**
   - Add more roles
   - Implement context retention
   - Enhance interface
   - Add sophisticated features

## 💡 Tips for Success

### For Basic Version:
1. Focus on core LangGraph concepts
2. Keep state structure simple
3. Test basic functionality first
4. Handle basic error cases

### For Advanced Version:
1. Build on basic concepts
2. Add features incrementally
3. Focus on state management
4. Implement robust error handling

---

**🎯 Remember**: Master the basics before moving to advanced features!

**Happy building!** 🚀