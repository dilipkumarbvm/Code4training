# 🔗 Module 1: Basic LangChain

**Foundation concepts for building AI applications with LangChain**

## 🎯 Learning Objectives

By the end of this module, you will understand:
- What LangChain is and why it's useful
- How to set up LangChain with OpenAI
- Basic LangChain Expression Language (LCEL) syntax
- How to create simple AI chains using the `|` operator
- The difference between raw AI responses and processed outputs

## 📁 Files in This Module

| File | Type | Description |
|------|------|-------------|
| `openai_langchain_example.py` | 🐍 Python | Interactive demo of basic LangChain concepts |
| `README.md` | 📖 Guide | This file - module overview and instructions |

## 🚀 Quick Start

### Prerequisites
```bash
# Make sure you're in the Week2 directory
cd Week2

# Install requirements
pip install -r requirements.txt

# Set up your API key
cp env_example.txt .env
# Edit .env file and add your OpenAI API key
```

### Run the Demo
```bash
python 01_basic_langchain/openai_langchain_example.py
```

## 🔑 Key Concepts Covered

### **LangChain Expression Language (LCEL)**
```python
# The magic of LangChain - chaining components with |
chain = prompt | model
result = chain.invoke({"topic": "artificial intelligence"})
```

### **Components You'll Learn**
- **🎯 Prompts** - Templates for AI instructions
- **🤖 Models** - AI engines (OpenAI GPT-4)
- **🔗 Chains** - Connecting prompts and models
- **📤 Raw Output** - Understanding `AIMessage` objects

## 💡 What Makes This Special

Unlike basic OpenAI API calls, LangChain provides:
- **🔗 Easy chaining** - Connect multiple components
- **📝 Template system** - Reusable prompt patterns  
- **🔄 Consistent interface** - Same pattern for different models
- **🧩 Modular design** - Build complex applications step by step

## 📚 Related Concepts

- **Environment Variables** - Secure API key management
- **Python dotenv** - Loading configuration from files
- **AI Message Objects** - Understanding structured AI responses
- **Error Handling** - Graceful failure when API keys are missing

## 🎓 Learning Tips

1. **Start Simple** - Run the demo first to see it working
2. **Experiment** - Try different topics in the user input
3. **Read the Code** - Every line is commented to explain what it does
4. **Check Output** - Notice the `AIMessage` structure vs simple text
5. **Build Foundation** - Master this before moving to Module 2

## ➡️ Next Steps

Once you understand basic chains, move to:
- **📝 Module 2** - Prompt Templates (more sophisticated prompts)
- **🔄 Module 3** - Output Parsers (structured data from AI)

## 🆘 Need Help?

- **📖 Main Documentation**: `../docs/JUPYTER_GUIDE.md`
- **📋 Exercises**: `../docs/TODO_week2.md`
- **⚠️ Common Issues**: Make sure your OpenAI API key is properly set in `.env`

---

**🎯 Goal**: Master the fundamentals before advancing to more complex LangChain features! 