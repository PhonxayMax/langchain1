# 🦜🔗 LangChain Course Project

A comprehensive LangChain learning project that demonstrates how to integrate various AI models using OpenRouter and LangChain framework.

## 📋 Table of Contents

- [🦜🔗 LangChain Course Project](#-langchain-course-project)
  - [📋 Table of Contents](#-table-of-contents)
  - [🎯 Project Overview](#-project-overview)
    - [📂 **Project Organization**](#-project-organization)
  - [✨ Features](#-features)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [📁 Project Structure](#-project-structure)
  - [🚀 Quick Start](#-quick-start)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set Up Python Environment](#2-set-up-python-environment)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Configure Environment Variables](#4-configure-environment-variables)
    - [5. Run the Main Example](#5-run-the-main-example)
  - [⚙️ Environment Setup](#️-environment-setup)
    - [Required Environment Variables](#required-environment-variables)
    - [Getting API Keys](#getting-api-keys)
  - [📄 File Descriptions](#-file-descriptions)
    - [🎯 Current Working Files (`from_1st_commit/`)](#-current-working-files-from_1st_commit)
    - [📦 Archive Files (`old_files_before_1st_commit/`)](#-archive-files-old_files_before_1st_commit)
    - [📋 Configuration Files](#-configuration-files)
  - [🔧 Configuration](#-configuration)
    - [Supported Models (via OpenRouter)](#supported-models-via-openrouter)
    - [Temperature Settings](#temperature-settings)
  - [💡 Usage Examples](#-usage-examples)
    - [Basic Chat](#basic-chat)
    - [With Prompt Templates](#with-prompt-templates)
  - [📚 Learning Resources](#-learning-resources)
    - [LangChain Documentation](#langchain-documentation)
    - [OpenRouter Resources](#openrouter-resources)
    - [Python Best Practices](#python-best-practices)
  - [🐛 Troubleshooting](#-troubleshooting)
    - [Common Issues](#common-issues)
      - [1. `ModuleNotFoundError: No module named 'langchain_openai'`](#1-modulenotfounderror-no-module-named-langchain_openai)
      - [2. `RuntimeError: Missing OPENROUTER_API_KEY in .env`](#2-runtimeerror-missing-openrouter_api_key-in-env)
      - [3. `Import "openai" could not be resolved`](#3-import-openai-could-not-be-resolved)
      - [4. Virtual Environment Issues](#4-virtual-environment-issues)
    - [Debug Mode](#debug-mode)
  - [🤝 Contributing](#-contributing)
    - [Code Style Guidelines](#code-style-guidelines)
  - [📜 License](#-license)
  - [📞 Support](#-support)

## 🎯 Project Overview

This project is part of a LangChain course that teaches how to:
- Integrate multiple AI providers through OpenRouter
- Use LangChain's powerful abstractions for AI applications
- Manage environment variables securely
- Structure Python projects for AI development

### 📂 **Project Organization**
The project is organized into logical folders:
- **`from_1st_commit/`**: Contains the current, working implementation
- **`old_files_before_1st_commit/`**: Archives experimental and earlier versions
- This structure helps track the evolution of the project and keeps the main codebase clean

## ✨ Features

- 🔌 **Multi-Provider Support**: Connect to various AI models through OpenRouter
- 🛡️ **Secure Configuration**: Environment-based API key management
- 🎨 **Clean Code Structure**: Well-organized, commented codebase
- 📝 **Multiple Examples**: Different approaches to AI integration
- 🚀 **Easy Setup**: Quick start with minimal configuration

## 🛠️ Technologies Used

- **Python 3.12+**: Core programming language
- **LangChain**: AI application framework
- **OpenRouter**: Multi-model AI API gateway
- **python-dotenv**: Environment variable management
- **Poetry**: Dependency management (pyproject.toml)

## 📁 Project Structure

```
langchain-course/
├── 📄 README.md                                    # This file - project documentation
├── 📄 pyproject.toml                               # Python project configuration
├── 📄 .env                                        # Environment variables (create this)
├── 📄 .gitignore                                  # Git ignore rules
├── 📄 .python-version                             # Python version specification
├── 📁 .venv/                                     # Virtual environment (auto-created)
├── � .git/                                      # Git repository data (hidden)
├── 📁 from_1st_commit/                           # ✨ Current working files
│   └── �📄 2025-10-13-7-44-Chat-Model-LC.py       # 🎯 Main LangChain example
└── 📁 old_files_before_1st_commit/               # 📦 Archive/experimental files
    ├── 📄 2025-10-13-7-44-Chat-Model.py          # Direct OpenAI integration
    ├── 📄 main.py                                # Early experiment
    └── 📄 main1.py                               # Early experiment
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd langchain-course
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows (PowerShell)
.venv\Scripts\Activate.ps1

# On Windows (CMD)
.venv\Scripts\activate.bat

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install langchain-openai python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

### 5. Run the Main Example
```bash
python from_1st_commit/2025-10-13-7-44-Chat-Model-LC.py
```

## ⚙️ Environment Setup

### Required Environment Variables

Create a `.env` file with the following variables:

```env
# ====================================
# AI API Configuration
# ====================================

# OpenAI API Key for GPT models
OPENAI_API_KEY=your_openai_key_here

# OpenRouter API Key (for multiple AI models)
OPENROUTER_API_KEY=your_openrouter_key_here

# Anthropic API Key for Claude models
ANTHROPIC_API_KEY=your_anthropic_key_here

# Base URLs
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

### Getting API Keys

1. **OpenRouter**: Visit [openrouter.ai](https://openrouter.ai) to get your API key
2. **OpenAI**: Visit [platform.openai.com](https://platform.openai.com) for direct OpenAI access
3. **Anthropic**: Visit [console.anthropic.com](https://console.anthropic.com) for Claude access

## 📄 File Descriptions

### 🎯 Current Working Files (`from_1st_commit/`)

- **`2025-10-13-7-44-Chat-Model-LC.py`**: 
  - ✨ **Main LangChain implementation** - This is the current working example
  - Uses OpenRouter for multi-model access
  - Well-commented for learning purposes with clear section separators
  - Demonstrates best practices for environment variable handling
  - Organized with professional code structure

### 📦 Archive Files (`old_files_before_1st_commit/`)

- **`2025-10-13-7-44-Chat-Model.py`**: 
  - Direct OpenAI integration example (before LangChain)
  - Comparison approach showing evolution of the project
  - Basic chat model usage without LangChain abstractions

- **`main.py` & `main1.py`**: 
  - Early experimental versions
  - Shows different approaches attempted during development
  - Kept for reference and learning progression

### 📋 Configuration Files

- **`pyproject.toml`**: Python project metadata and dependencies
- **`.env`**: Environment variables (you need to create this - not tracked by Git)
- **`.python-version`**: Specifies Python version (3.12+) for the project
- **`.gitignore`**: Protects sensitive files from being committed to Git

## 🔧 Configuration

### Supported Models (via OpenRouter)

```python
# Available models you can use:
models = [
    "openai/gpt-4o",           # GPT-4 Omni
    "openai/gpt-4o-mini",      # GPT-4 Omni Mini
    "anthropic/claude-3-sonnet", # Claude 3 Sonnet
    "google/gemini-pro",       # Gemini Pro
    # ... and many more
]
```

### Temperature Settings

```python
temperature_guide = {
    0.0: "Deterministic, consistent responses",
    0.3: "Focused, mostly consistent", 
    0.7: "Creative, balanced (recommended)",
    1.0: "Very creative, more random"
}
```

## 💡 Usage Examples

### Basic Chat
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key=openrouter_api_key,
    base_url=openrouter_base_url,
    model="openai/gpt-4o-mini",
    temperature=0.7
)

response = llm.invoke("What is the capital of Thailand?")
print(response.content)
```

### With Prompt Templates
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{user_input}")
])

chain = prompt | llm
response = chain.invoke({"user_input": "Hello!"})
```

## 📚 Learning Resources

### LangChain Documentation
- [Official LangChain Docs](https://docs.langchain.com/)
- [LangChain Python API Reference](https://api.python.langchain.com/)

### OpenRouter Resources
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Supported Models](https://openrouter.ai/models)

### Python Best Practices
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Environment Variables](https://docs.python.org/3/library/os.html#os.environ)

## 🐛 Troubleshooting

### Common Issues

#### 1. `ModuleNotFoundError: No module named 'langchain_openai'`
**Solution**: Install the required package
```bash
pip install langchain-openai
```

#### 2. `RuntimeError: Missing OPENROUTER_API_KEY in .env`
**Solution**: 
- Create a `.env` file in the project root
- Add your OpenRouter API key: `OPENROUTER_API_KEY=your_key_here`

#### 3. `Import "openai" could not be resolved`
**Solution**: Install dependencies
```bash
pip install openai python-dotenv langchain-openai
```

#### 4. Virtual Environment Issues
**Solution**: Recreate the virtual environment
```bash
# Remove existing environment
rm -rf .venv  # Linux/macOS
rmdir /s .venv  # Windows

# Create new environment
python -m venv .venv
# Activate and install dependencies
```

### Debug Mode

Add this to your code for more detailed error information:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style Guidelines

- Follow PEP 8 conventions
- Add comments for complex logic
- Use the established separator style:
  ```python
  # ============================================================================
  # SECTION NAME
  # ============================================================================
  ```
- Include docstrings for functions and classes

## 📜 License

This project is part of a learning course. Feel free to use it for educational purposes.

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the [LangChain documentation](https://docs.langchain.com/)
3. Create an issue in this repository

---

**Happy Learning! 🚀**

Made with ❤️ for AI learning
