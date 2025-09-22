# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python-based AI training repository containing weekly modules that progress from basic chatbot implementations to advanced AI application architectures using LangChain, LangGraph, and MCP (Model Context Protocol) systems.

## Common Development Commands

### Environment Setup
```bash
# Create conda environment for the course
conda create -n code4training python=3.12
conda activate code4training

# Navigate to specific week and install dependencies
cd Week[X]/[project_name]
pip install -r requirements.txt
```

### Running Applications
```bash
# Basic chatbots (Week 1)
python ai_chatbot.py

# LangChain demos (Week 2)
python [module_name]_demo.py

# Interactive notebooks (Week 2, 4)
jupyter notebook

# MCP servers (Week 7)
python email_processor.py
```

### Environment Variables
All projects require API keys set via environment variables or `.env` files:
- `OPENAI_API_KEY` (most projects)
- `ANTHROPIC_API_KEY` (Anthropic chatbot)

Copy `env_example.txt` to `.env` and add your keys.

## Code Architecture

### Week-by-Week Structure

#### Week 1: Foundation Chatbots
- **anthropic-chatbot/**: Claude-based chatbot using Anthropic API
- **openai-chatbot/**, **simple_openai/**: OpenAI-based implementations
- Architecture: Simple request-response loops with basic error handling
- Key pattern: Environment variable loading → API client initialization → Chat loop

#### Week 2: LangChain Applications
- **Five progressive modules**: 01_basic_langchain → 05_document_loaders
- Architecture: Chain-based programming using LangChain Expression Language (LCEL)
- Key pattern: `prompt | model | parser` chains
- Dual format: Both `.py` scripts and Jupyter notebooks for each concept
- Output parsers: String, JSON, and Pydantic for structured data

#### Week 4: LangGraph Workflows  
- **notebooks/**: Jupyter-based LangGraph implementations
- Architecture: State-based workflow graphs for complex multi-step AI processes
- Key pattern: Node-based workflow graphs with persistence and state management

#### Week 7: MCP (Model Context Protocol) Systems
- **email_processor/**, **support_center/**: Production-ready MCP servers
- Architecture: FastMCP-based servers with async operations, database integration
- Key pattern: MCP server → Pydantic models → OpenAI integration → Database operations

### Common Patterns

#### Error Handling
- Graceful API key validation with user-friendly messages
- Try-catch blocks around API calls with retry suggestions
- Keyboard interrupt handling for clean exits

#### Data Models
- Pydantic models for structured data validation (Week 2+)
- Type hints throughout for better code quality
- BaseModel inheritance for consistent data structures

#### API Integration
- Consistent async/await patterns for API calls in advanced modules
- Environment variable management with python-dotenv
- Multiple AI provider support (OpenAI, Anthropic)

## Development Workflow

### When Working with This Codebase

1. **Identify the week/module** you're working with
2. **Check requirements.txt** for that specific module's dependencies
3. **Look for env_example.txt** or similar for required environment variables
4. **Follow the progressive learning path** - later weeks build on earlier concepts
5. **Use appropriate format**: Scripts for quick execution, notebooks for exploration

### Module Dependencies

- **Week 1**: Basic Python, openai/anthropic packages
- **Week 2**: LangChain ecosystem (langchain, langchain-openai, langchain-community)
- **Week 4**: LangGraph, Jupyter notebooks
- **Week 7**: FastMCP, async programming, SQL integration

### File Naming Conventions

- `*_demo.py`: Demonstration scripts for specific concepts
- `*.ipynb`: Jupyter notebooks for interactive learning
- `requirements.txt`: Module-specific dependencies
- `env_example.txt`: Template for environment variables
- `README.md`: Module-specific documentation

## Testing and Validation

### No Automated Test Suite
This repository does not contain automated tests. Validation is done through:
- Manual execution of demo scripts
- Interactive notebook exploration
- Functional testing of chatbot responses

### When Making Changes
- Test changes by running the specific module's demo script
- For notebooks: Execute all cells to ensure proper functionality  
- Verify API integrations work with test inputs
- Check error handling by testing with invalid inputs

## Key Technologies

- **AI APIs**: OpenAI (primary), Anthropic Claude
- **Frameworks**: LangChain (Week 2+), LangGraph (Week 4+), FastMCP (Week 7)
- **Data**: Pydantic for validation, SQLAlchemy for persistence
- **Environment**: Conda/pip, python-dotenv, Jupyter
- **Development**: Progressive complexity from simple scripts to production-ready servers