# 📚 Jupyter Notebooks Guide

Welcome to the **interactive Jupyter notebook versions** of our LangChain demos! These notebooks provide a much better learning experience than console programs.

## 🎯 Why Jupyter Notebooks?

### **🔥 Benefits over Console Programs:**
- ✅ **Visual and Interactive** - See code and output together
- ✅ **Easy to Experiment** - Modify variables and re-run cells
- ✅ **Rich Documentation** - Markdown explanations alongside code
- ✅ **Step-by-Step Learning** - Run one concept at a time
- ✅ **Save Your Work** - Keep notes and modifications
- ✅ **No Terminal Required** - Everything in the browser

### **📊 Console vs Notebook Comparison:**

| Feature | Console Program | Jupyter Notebook |
|---------|----------------|------------------|
| **Interactivity** | Run all at once | Run cell by cell |
| **Experimentation** | Edit file, re-run all | Change variables, re-run section |
| **Documentation** | Comments only | Rich markdown + code |
| **Visual Appeal** | Plain text | Formatted output, tables, diagrams |
| **Learning** | Linear progression | Explore at your own pace |

## 📁 Available Notebooks

### **1. Prompting Techniques Demo** (`prompting_techniques_demo.ipynb`)
- **Topic:** Different prompting approaches (zero-shot, few-shot, chain-of-thought, role)
- **Example:** Customer support email classification
- **Key Learning:** How the way you ask affects what you get

### **2. Prompt Templates Demo** (`prompt_templates_demo.ipynb`)  
- **Topic:** Different template structures and their effects
- **Example:** All templates use "artificial intelligence" as the topic
- **Key Learning:** How template design affects response style

## 🚀 Getting Started

### **1. Install Requirements**
```bash
cd Week2
pip install -r requirements.txt
```
*(This now includes Jupyter)*

### **2. Set Up API Key**
Create a `.env` file:
```bash
cp env_example.txt .env
# Edit .env and add your OpenAI API key
```

### **3. Start Jupyter**
```bash
jupyter notebook
```
**→ Opens in your browser automatically!**

### **4. Open a Notebook**
- Click on `prompting_techniques_demo.ipynb` or `prompt_templates_demo.ipynb`
- Follow the step-by-step instructions

## 🎓 How to Use the Notebooks

### **📖 Reading Structure:**
1. **Markdown cells** (like this) contain explanations and theory
2. **Code cells** contain executable Python code
3. **Output cells** show the results when you run code

### **⚡ Running Cells:**
- **Click a cell** to select it
- **Press Shift+Enter** to run the cell and move to the next
- **Press Ctrl+Enter** to run the cell and stay on it

### **🔧 Experimenting:**
1. **Start from the top** - Run the setup cell first
2. **Run cells in order** - Each builds on the previous
3. **Try modifications:**
   - Change the `TOPIC` variable in prompt templates demo
   - Modify the customer email in prompting techniques demo
   - Edit system messages to create different AI personas
4. **Re-run cells** to see how changes affect output

## 🎨 Visual Learning Features

### **📊 Structured Output:**
Instead of plain text, you get:
- **Headers and sections** for easy navigation
- **Tables** comparing different techniques
- **Highlighted code blocks** with syntax coloring
- **Formatted responses** that are easy to read

### **🔍 Side-by-Side Comparisons:**
Each notebook shows the **same input** with **different techniques** so you can clearly see:
- How zero-shot vs few-shot affects responses
- How basic templates vs complex instructions change output style
- How conversation history influences AI behavior

## 💡 Learning Tips

### **🎯 Best Practices:**
1. **Read explanations first** - Understand the concept before running code
2. **Run cells in order** - Each builds on previous setup
3. **Experiment freely** - Notebooks are perfect for trying variations
4. **Take notes** - Add your own markdown cells with observations
5. **Save frequently** - `Ctrl+S` to save your progress

### **🧪 Experiments to Try:**
- **Change topics** - Try "machine learning", "blockchain", "climate change"
- **Modify personas** - Make the AI act like a doctor, lawyer, comedian
- **Add conversation history** - Create longer dialogue contexts
- **Create new examples** - Use your own real-world scenarios

## 🛠️ Troubleshooting

### **"Kernel not found" Error:**
```bash
python -m ipykernel install --user --name=python3
```

### **"Module not found" Error:**
```bash
pip install -r requirements.txt
```

### **API Key Issues:**
- Check your `.env` file format
- Make sure the key is valid
- Verify internet connection

### **Notebook Won't Open:**
```bash
# Try a different port
jupyter notebook --port 8889
```

## 🔄 Converting Console Programs to Notebooks

If you want to convert other `.py` files to notebooks:

### **Manual Method:**
1. Create new notebook in Jupyter
2. Copy code sections into code cells
3. Add markdown explanations between code
4. Test and refine

### **Automatic Method:**
```bash
# Install converter
pip install nbconvert

# Convert (creates basic notebook)
jupyter nbconvert --to notebook your_script.py
```

## 🎉 Next Steps

1. **Start with prompting techniques** - Great introduction to LangChain concepts
2. **Try prompt templates** - Learn how structure affects responses  
3. **Experiment with modifications** - Make them your own
4. **Create your own notebooks** - Apply concepts to your projects
5. **Share your discoveries** - Notebooks are great for showing others your work

---

**🎓 Jupyter notebooks make learning LangChain interactive, visual, and fun!** 

**Happy experimenting!** 🚀 