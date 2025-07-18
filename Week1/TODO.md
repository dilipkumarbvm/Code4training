# Week 1 Take-Home Exercises

These exercises are designed to help you practice and extend your understanding of the AI chatbot project. Choose 2-3 exercises that interest you most.

## Exercise 1: Personality Customization

**Goal**: Give your chatbot a unique personality

**Tasks**:
- Add a "system" message to give the AI a specific personality
- Try different personalities: helpful teacher, friendly poet, comedy assistant, wise philosopher
- Experiment with different greeting messages
- Test how the personality affects responses to the same questions

**Example System Message**:
```python
messages=[
    {"role": "system", "content": "You are a helpful coding teacher who explains things simply and encourages students."},
    {"role": "user", "content": user_input}
]
```

---

## Exercise 2: Parameter Experimentation

**Goal**: Understand how API parameters affect AI responses

**Tasks**:
- Change `temperature` values:
  - 0.1 (very focused and consistent)
  - 0.7 (balanced - current setting)
  - 0.9 (very creative and varied)
- Adjust `max_tokens`:
  - 50 (short responses)
  - 150 (current setting)
  - 300 (longer responses)
- Try different models: `gpt-3.5-turbo` vs `gpt-4o-mini`

**Deliverable**: Create a small comparison document showing how each change affects responses to the same question.

---

## Exercise 3: User Interface Improvements

**Goal**: Make the chatbot more user-friendly

**Tasks**:
- Change the emojis (🤖 → 🧠, 👤 → 😊, or create your own theme)
- Add a custom welcome message explaining what your bot does
- Create a personalized goodbye message
- Add a "thinking..." indicator while waiting for responses
- Improve the visual formatting of conversations

**Example Enhancement**:
```python
print("🧠 AI Assistant: Thinking...")
# API call here
print(f"🧠 AI Assistant: {ai_response}")
```

---

## Exercise 4: Input Validation

**Goal**: Make the chatbot handle user input better

**Tasks**:
- Prevent sending messages that are too short (e.g., less than 3 characters)
- Add more exit commands ("stop", "done", "finish", "end")
- Set a character limit and warn users if they exceed it
- Handle special characters or unusual input gracefully
- Add confirmation for exit commands

**Example Validation**:
```python
if len(user_input) < 3:
    print("Please enter a message with at least 3 characters.")
    continue
```

---

## Exercise 5: Simple Statistics

**Goal**: Track basic usage information

**Tasks**:
- Count how many messages were sent in the conversation
- Display the count when exiting
- Add timestamps to messages
- Show conversation duration (start time to end time)
- Display a summary when the user quits

**Example Output**:
```
👋 Goodbye!
📊 Conversation Summary:
   • Messages exchanged: 12
   • Duration: 5 minutes, 23 seconds
   • Started: 2:45 PM
```

---

## Exercise 6: Prompt Templates

**Goal**: Create shortcuts for common requests

**Tasks**:
- Add shortcuts like `/joke` → "Tell me a joke"
- `/explain [topic]` → "Explain this topic simply"
- `/poem [subject]` → "Write a poem about this"
- `/story` → "Tell me a short story"
- Create a help command (`/help`) that lists all shortcuts

**Example Implementation**:
```python
if user_input.startswith('/joke'):
    user_input = "Tell me a clean, funny joke"
elif user_input.startswith('/explain '):
    topic = user_input[9:]  # Remove '/explain '
    user_input = f"Explain {topic} in simple terms"
```

---

## Exercise 7: Error Message Customization

**Goal**: Improve error handling and user guidance

**Tasks**:
- Add custom error messages for different scenarios
- Create helpful hints when things go wrong
- Add retry suggestions for common errors
- Provide troubleshooting tips in user-friendly language
- Handle network timeouts gracefully

**Example Custom Error**:
```python
except Exception as e:
    if "rate limit" in str(e).lower():
        print("🚦 Slow down! You're sending messages too quickly. Try again in a moment.")
    else:
        print(f"🔧 Oops! Something went wrong: {e}")
        print("💡 Try checking your internet connection or API key.")
```

---

## Sample Take-Home Assignment Structure

**"Customize Your Chatbot" - Choose 2-3 exercises above**

### What to Submit:

1. **Modified Python File**: Your updated `ai_chatbot.py` with your chosen enhancements
2. **Screenshot**: Show your chatbot in action with your improvements
3. **Written Summary** (1-2 paragraphs):
   - What you changed and why
   - What you learned from the process
   - Any challenges you encountered

### Grading Criteria:

- ✅ Code runs without errors
- ✅ Improvements are functional and demonstrate understanding
- ✅ Clear explanation of changes made
- ✅ Evidence of experimentation and learning

---

## Learning Objectives

These exercises help you practice:

- **Code Modification**: Safely changing existing working code
- **API Understanding**: How parameters affect AI behavior
- **User Experience**: Making software more intuitive and friendly
- **Python Fundamentals**: String manipulation, conditionals, error handling
- **Documentation**: Explaining your work clearly
- **Problem Solving**: Debugging and improving functionality

## Tips for Success

1. **Start Small**: Pick one exercise and get it working before moving to the next
2. **Test Frequently**: Run your code after each change to catch errors early
3. **Save Backups**: Keep a copy of the working original code
4. **Read Error Messages**: They often tell you exactly what went wrong
5. **Experiment**: Try different values and see what happens
6. **Ask Questions**: If stuck, note what you tried and ask for help

## Bonus Challenge

For those who complete all exercises: Try combining multiple enhancements to create a truly unique chatbot experience. For example, a poetry bot with custom shortcuts, personality, and conversation statistics!

---

**Remember**: The goal is to learn and experiment. Don't worry if everything isn't perfect - the important thing is understanding how the code works and what each change accomplishes. 