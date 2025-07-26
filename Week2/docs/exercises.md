# 🚀 Week 2 Real-World Exercises

**Build practical AI applications by combining all LangChain concepts you've learned**

## 🎯 Learning Approach

These exercises combine **all 3 modules** into real-world applications. Each exercise challenges you to apply multiple concepts together, just like in professional development.

**Your Mission**: Use the demos and READMEs as reference, but build these applications yourself!

---

## 📋 Prerequisites

✅ **Complete all 3 modules** (01-03) in Week2  
✅ **API Key Setup** - Your `.env` file with `OPENAI_API_KEY`  
✅ **Dependencies** - Run `pip install -r requirements.txt`  

---

## 🔍 Exercise 1: AI Website Analyzer
**Combines: Document Loaders + Role Prompting + JSON Output**

### 🎯 What You'll Build
A tool that analyzes any website from different professional perspectives.

### 📝 Your Task
Create `website_analyzer.py` that:

1. **Ask user for a website URL**
2. **Load the webpage content** using WebBaseLoader
3. **Ask user to choose an expert role:**
   - Marketing Expert
   - Business Analyst  
   - UX Designer
   - Content Strategist
4. **Analyze the website** using role prompting
5. **Output structured results** as JSON with:
   - Main topic
   - Target audience
   - 3 key insights
   - Professional recommendation
   - Quality score (1-10)

### 💡 Prompt Building Hints

**🎭 Role Prompting Structure:**
```
"You are an experienced {role} with 10+ years in the industry. 
Analyze this website content: {content}
Focus on {role-specific aspects}..."
```

**📋 JSON Output Guidance:**
- Tell the AI exactly what JSON structure you want
- Use `get_format_instructions()` from your JSON parser
- Include example JSON in your prompt if needed

**🔍 Analysis Prompting Tips:**
- Ask for specific, measurable insights
- Request professional terminology for each role
- Guide the AI to focus on role-relevant aspects:
  - **Marketing Expert**: audience, messaging, conversion potential
  - **Business Analyst**: value proposition, competitive advantages  
  - **UX Designer**: usability, accessibility, user flow
  - **Content Strategist**: content quality, SEO, engagement

### 🧪 Test Your Solution
Try analyzing:
- A news website (BBC, CNN)
- A company homepage (Apple, Microsoft)
- A blog or documentation site

### 🎯 Success Criteria
- Works with any valid URL
- Different expert roles give different insights
- Clean, structured JSON output
- Handles basic errors gracefully

---

## 📧 Exercise 2: Smart Email Classifier
**Combines: Prompt Templates + Chain-of-Thought + Few-Shot Examples**

### 🎯 What You'll Build
A customer service tool that classifies and suggests responses for customer emails.

### 📝 Your Task
Create `email_classifier.py` that:

1. **Present sample customer emails** (or let user paste their own):
   - A complaint about delayed shipping
   - A technical support question
   - A compliment about good service
   - A refund request

2. **Use Chain-of-Thought prompting** to analyze:
   - What type of email is this?
   - How urgent is it?
   - What's the customer's mood?
   - Which department should handle it?

3. **Use Few-Shot prompting** to generate appropriate response suggestions

4. **Show the analysis step-by-step** so users understand the reasoning

### 💡 Prompt Building Hints

**🧠 Chain-of-Thought Structure:**
```
"Let's analyze this email step by step:
1. First, read the email content carefully
2. Identify the main request or concern
3. Assess the customer's emotional tone
4. Determine urgency level (1-5)
5. Classify the email type
6. Recommend which department should handle it"
```

**📚 Few-Shot Examples Pattern:**
```
"Here are examples of good customer service responses:

Email Type: Complaint
Sample Response: 'Thank you for bringing this to our attention...'

Email Type: Technical Question  
Sample Response: 'I'd be happy to help you with...'

Now analyze this email: {email_content}"
```

**🎯 Classification Prompting Tips:**
- Define clear categories (complaint, question, compliment, refund, etc.)
- Ask for confidence scores for each classification
- Request specific reasoning for each step
- Include urgency scale definitions (1=low, 5=critical)

**💬 Response Generation Guidance:**
- Ask for professional, empathetic tone
- Request specific action items for the customer service agent
- Include escalation recommendations when needed

### 🧪 Test Your Solution
Create different types of customer emails and see if your classifier:
- Correctly identifies the category
- Suggests appropriate responses
- Handles different tones (angry, happy, neutral)

### 🎯 Success Criteria
- Accurate email classification
- Clear step-by-step reasoning
- Professional response suggestions
- Works with different email types

---

## 🎨 Exercise 3: Content Creator Assistant
**Combines: Web Research + Creative Prompting + Structured Output**

### 🎯 What You'll Build
A tool that helps create content by researching topics and generating structured ideas.

### 📝 Your Task
Create `content_assistant.py` that:

1. **Ask user for a content topic** (blog post, video, presentation, etc.)

2. **Research the topic** by loading 2-3 relevant websites

3. **Generate content ideas** using different prompting techniques:
   - Zero-shot: Quick brainstorming
   - Few-shot: Ideas similar to successful content
   - Chain-of-thought: Step-by-step content planning

4. **Output structured content plan** with:
   - Title suggestions
   - Key points to cover
   - Target audience
   - Content outline
   - Research sources used

### 💡 Prompt Building Hints

**🔬 Research Integration:**
```
"Based on this research from {source_urls}:
{website_content}

Create content about: {topic}"
```

**🎯 Zero-Shot Brainstorming:**
```
"Generate 5 creative title ideas for content about {topic}.
Make them engaging and clickable for {target_audience}."
```

**📝 Few-Shot Content Planning:**
```
"Here are examples of successful content structures:

Topic: 'Remote Work Tips'
Structure: Problem → Solution → Action Steps → Results

Topic: 'Cooking Basics'  
Structure: Overview → Ingredients → Step-by-step → Troubleshooting

Now create a similar structure for: {your_topic}"
```

**🧠 Chain-of-Thought Planning:**
```
"Let's plan this content step by step:
1. Who is the target audience for this topic?
2. What's their main problem or interest?
3. What key points must we cover?
4. How should we structure the information?
5. What examples or stories would help?
6. What action should readers take after?"
```

**📋 Structured Output Tips:**
- Request specific sections (Introduction, Main Points, Conclusion)
- Ask for target word counts or time lengths
- Include SEO considerations (keywords, meta descriptions)
- Request different content formats (blog, video script, presentation)

### 🧪 Test Your Solution
Try creating content about:
- "Sustainable cooking tips"
- "Remote work productivity"
- "Learning Python programming"

### 🎯 Success Criteria
- Incorporates relevant research from web sources
- Generates creative, useful content ideas
- Uses multiple prompting techniques effectively
- Provides actionable content outlines

---

## 💡 Tips for Success

### **🔧 Implementation Strategy**
1. **Start simple** - Get basic functionality working first
2. **Use module demos as reference** - Don't reinvent the wheel
3. **Test frequently** - Make sure each piece works before adding complexity
4. **Handle errors gracefully** - What happens with bad URLs or network issues?

### **🎯 Learning Approach**
- **Read the module READMEs** when you need to remember concepts
- **Experiment freely** - Try different prompts and see what works
- **Combine techniques** - The magic happens when you mix different approaches
- **Make it useful** - Build something you'd actually want to use

### **🆘 When You Get Stuck**
- Review the relevant module demo code
- Check the module README for guidance
- Start with a simpler version and build up
- Test individual components before combining them

---

## 🚀 What's Next?

After completing these exercises:
- **🏗️ Build your own projects** using these patterns
- **💼 Add these projects to your portfolio** - they demonstrate real skills
- **🌟 Share your creations** - help other learners see what's possible

---

**🎯 Remember**: The goal isn't perfect code - it's building practical AI applications that solve real problems!

**Happy building!** 🚀 