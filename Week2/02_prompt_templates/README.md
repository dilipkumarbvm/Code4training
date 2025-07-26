# 📝 Module 2: Prompt Templates

**Learn how different prompt structures dramatically affect AI responses**

## 🎯 Learning Objectives

By the end of this module, you will understand:
- How prompt structure affects AI behavior and response style
- Different types of LangChain prompt templates
- The power of system messages vs user messages
- How to include conversation history in prompts
- When to use each template type for different use cases

## 📁 Files in This Module

| File | Type | Description |
|------|------|-------------|
| `prompt_templates_demo.py` | 🐍 Python | Console demo comparing 4 template types |
| `prompt_templates_demo.ipynb` | 📓 Jupyter | Interactive notebook with rich formatting |
| `README.md` | 📖 Guide | This file - module overview and instructions |

## 🚀 Quick Start

### Option 1: Console Demo
```bash
python 02_prompt_templates/prompt_templates_demo.py
```

### Option 2: Interactive Notebook (Recommended)
```bash
# Start Jupyter
jupyter notebook

# Open: 02_prompt_templates/prompt_templates_demo.ipynb
# Run cells step by step for best learning experience
```

## 🔑 Key Template Types Covered

### **1. 🔗 Basic String Template**
```python
template = PromptTemplate.from_template("Tell me a fact about {topic}")
# Result: Simple, direct responses
```

### **2. 💬 Chat Template (with System Message)**
```python
template = ChatPromptTemplate([
    ("system", "You are a helpful teacher"),
    ("user", "Explain {topic} in simple terms")
])
# Result: Educational, teacher-style responses
```

### **3. 📚 Template with Conversation History**
```python
template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("history"),
    ("user", "{question}")
])
# Result: Contextual responses that reference previous conversation
```

### **4. 📋 Complex Template with Detailed Instructions**
```python
template = ChatPromptTemplate([
    ("system", """You are an expert consultant. When explaining:
    1. Start with a clear definition
    2. Provide 2-3 key applications  
    3. End with future implications"""),
    ("user", "Provide a comprehensive overview of {topic}")
])
# Result: Structured, professional analysis
```

## 💡 The Magic of Different Templates

**Same Input ("artificial intelligence"), Very Different Outputs:**

| Template Type | Response Style | Best For |
|---------------|----------------|----------|
| **Basic** | Direct facts | Quick information |
| **Chat** | Educational explanations | Teaching/learning |
| **With History** | Contextual & personalized | Ongoing conversations |
| **Complex** | Structured & comprehensive | Professional reports |

## 🎓 Key Learning Insights

### **System Messages Are Powerful**
- They set the AI's "personality" and behavior
- AI adopts the role you specify (teacher, consultant, etc.)
- Different roles produce dramatically different response styles

### **Context Matters**
- Conversation history influences future responses
- AI builds on previous interactions naturally
- `MessagesPlaceholder` makes this easy to implement

### **Detailed Instructions Work**
- Specific formatting requests are followed
- Numbered steps in system messages create structure
- Professional roles enhance response quality

## 🧪 Experiments to Try

1. **Change the topic** - Try "machine learning", "climate change", "cooking"
2. **Modify system messages** - Make the AI act like a doctor, comedian, or scientist
3. **Add more conversation history** - See how it influences responses
4. **Create your own templates** - Design prompts for your specific use cases

## 📚 Related Concepts

- **Message Roles** - System, User, Assistant message types
- **Variable Substitution** - Using `{variable}` placeholders
- **Chain Construction** - `template | model` pattern
- **Response Comparison** - Understanding how prompts affect outputs

## 🎓 Learning Tips

1. **Use the Notebook** - Visual comparison makes differences clear
2. **Run Sequentially** - See how same topic produces different responses
3. **Read All Outputs** - Notice tone, structure, and content differences
4. **Experiment Freely** - Change variables and see what happens
5. **Compare Styles** - This is the key learning objective

## ➡️ Next Steps

Once you master prompt templates:
- **🔄 Module 3** - Output Parsers (structure the responses you get)
- **🎯 Module 4** - Prompting Techniques (advanced strategies)

## 🆘 Need Help?

- **📖 Jupyter Guide**: `../docs/JUPYTER_GUIDE.md`
- **📋 Practice Exercises**: `../docs/TODO_week2.md`
- **⚠️ Not seeing differences?** Make sure you're using the same topic across all templates

---

**🎯 Goal**: Understand how prompt structure is as important as the AI model itself! 