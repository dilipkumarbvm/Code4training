# Week 2 TODO - LangChain Practice Exercises

## 🎯 Learning Objectives
By completing these exercises, you will:
- Practice using different LangChain output parsers
- Create reusable prompt templates
- Load and process external content with document loaders

## 📚 Prerequisites
- Complete all demo files in Week2 folder
- Have your `.env` file set up with OpenAI API key

---

## Exercise 1: Output Parsers Practice 📝

### Goal
Create a simple application that uses different output parsers.

### Your Task
Create a file called `output_parsers_exercise.py` that:

1. **Create a Recipe Generator:**
   - Takes a cuisine type as input (e.g., "Italian", "Mexican")
   - Generates a recipe using the AI
   - Uses different output parsers for different formats

2. **Features to implement:**
   ```python
   # Option 1: List format (ingredients list)
   from langchain.output_parsers import CommaSeparatedListOutputParser
   
   # Option 2: JSON format (full recipe)
   # https://python.langchain.com/docs/how_to/output_parser_json/
   from langchain.output_parsers.json import SimpleJsonOutputParser
   ```

3. **Requirements:**
   - Ask user to choose format: "list" or "json"
   - For list: return ingredients as a Python list
   - For JSON: return recipe with keys: name, ingredients, instructions, prep_time
   - Display the results clearly

### Expected Output
```
Choose format (list/json): list
Output: ['tomatoes', 'pasta', 'olive oil', 'garlic', 'basil']

Choose format (list/json): json  
Output: {'name': 'Spaghetti Marinara', 'ingredients': [...], 'instructions': '...', 'prep_time': '30 minutes'}
```

### Hints
- Use `get_format_instructions()` in your prompts
- Start with the demos you've already completed
- Test with different cuisine types

---

## Exercise 2: Prompt Templates Practice 📄

### Goal
Create flexible prompt templates for different scenarios.

### Your Task
Create a file called `prompt_templates_exercise.py` that:

1. **Create a Language Learning Assistant:**
   - Helps users practice different languages
   - Adapts to different skill levels
   - Maintains conversation context

2. **Template Requirements:**
   ```python
   ChatPromptTemplate([
       ("system", "You are a {language} teacher for {level} students"),
       MessagesPlaceholder("conversation"),
       ("user", "{user_message}")
   ])
   ```

3. **Features to implement:**
   - User selects language (Spanish, French, German, etc.)
   - User selects level (beginner, intermediate, advanced)
   - Maintains simple conversation history
   - Provides helpful corrections and tips

### Expected Features
- Language and level selection
- At least 3 conversation exchanges
- Context preservation between messages
- Clear, educational responses

### Hints
- Start simple with just 2-3 languages
- Use MessagesPlaceholder for conversation history
- Test different combinations of language and level

---

## Exercise 3: Document Loaders Practice 🌐

### Goal
Create a web content summarizer using document loaders.

### Your Task
Create a file called `document_loaders_exercise.py` that:

1. **Create a Simple Article Summarizer:**
   - Takes a URL from the user
   - Loads the webpage content
   - Provides a summary using AI

2. **Features to implement:**
   ```python
   from langchain_community.document_loaders import WebBaseLoader
   
   # Load content
   loader = WebBaseLoader(user_url)
   documents = loader.load()
   
   # Summarize with AI
   summary = chain.invoke({"content": documents[0].page_content})
   ```

3. **Requirements:**
   - Accept URL input from user
   - Handle basic errors (invalid URLs, network issues)
   - Generate a clear summary (2-3 paragraphs)
   - Display both original content length and summary

### Expected Features
- URL input validation
- Error handling for failed loads
- Content length information
- Clear summary output

### Hints
- Start with simple news websites or blogs
- Truncate very long content before sending to AI
- Test with different types of websites

---

## 🔍 Testing Your Solutions

### Test Cases:
1. **Output Parsers:** Try different cuisines and both output formats
2. **Prompt Templates:** Test multiple languages and skill levels
3. **Document Loaders:** Try news sites, blogs, and documentation pages

### Validation Checklist:
- [ ] Code runs without errors
- [ ] Handles user input properly
- [ ] Includes basic error handling
- [ ] Produces expected output formats
- [ ] Works with different inputs

---

## 📖 Quick Reference

### Key Imports:
```python
# Output Parsers
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.output_parsers.json import SimpleJsonOutputParser

# Prompt Templates  
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Document Loaders
from langchain_community.document_loaders import WebBaseLoader
```

### Common Patterns:
```python
# Basic chain pattern
chain = prompt_template | model | output_parser
result = chain.invoke(input_data)

# With conversation history
template = ChatPromptTemplate([
    ("system", "..."),
    MessagesPlaceholder("history"),
    ("user", "{message}")
])
```

## Exercise 4: Prompting Techniques Practice 🎯

### Goal
Practice different prompting techniques and understand when to use each approach.

### Your Task
Create a file called `prompting_exercise.py` that:

1. **Create a Medical Symptom Checker** using all 4 prompting techniques:
   - Use the same patient description: "I have a headache, fever, and sore throat for 3 days"
   - Apply zero-shot, few-shot, chain-of-thought, and role prompting
   - Compare the different responses

2. **Your Implementation Should Include:**
   ```python
   # Zero-shot: Direct question
   def check_symptoms_zero_shot(symptoms):
       # Simple prompt asking for possible conditions
   
   # Few-shot: Provide examples
   def check_symptoms_few_shot(symptoms):
       # Include 2-3 example symptom → condition pairs
   
   # Chain-of-thought: Step-by-step analysis  
   def check_symptoms_cot(symptoms):
       # Ask AI to analyze step by step
   
   # Role prompting: Act as medical professional
   def check_symptoms_role(symptoms):
       # AI acts as experienced nurse or doctor
   ```

3. **Bonus Challenge:**
   - Try the same techniques with a different domain (legal advice, cooking tips, etc.)
   - Notice how the quality and style of responses change

### Expected Output
Each technique should produce different styles of responses, showing how prompting approach affects AI behavior.

### Learning Outcome
Understanding that **how you ask** is as important as **what you ask** in AI interactions.

---

## ✅ Submission

Once you complete the exercises:
1. Test with different inputs
2. Add comments explaining your code
3. Make sure error handling works

**Goal:** Build confidence with LangChain fundamentals through practical, achievable projects.

---

**Happy Coding! 🎉** 