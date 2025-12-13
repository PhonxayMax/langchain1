# LangChain Course Project

A LangChain learning project demonstrating AI model integration using OpenRouter and LangChain framework.

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/PhonxayMax/langchain1.git
cd langchain1
```

### 2. Set Up Environment

**Using uv (recommended):**
```bash
uv venv .venv
uv pip install -r requirements.txt
```

**Using pip:**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:
```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
NAGA_API_KEY=your_naga_key_here
NAGA_BASE_URL=https://api.naga.ai/v1
```

Get your API key at [openrouter.ai](https://openrouter.ai)

### 4. Run Example
```bash
python from_1st_commit/2025-10-13-7-44-Chat-Model-LC.py
```

## Project Structure

```
langchain1/
├── from_1st_commit/               # Main examples
│   ├── 2025-10-13-7-44-Chat-Model-LC.py
│   ├── kongruksiam/              # Additional examples
│   └── rag/                      # RAG implementations
├── old_files_before_1st_commit/  # Archive files
├── id_7_2025-10-17-20-29/        # Jupyter notebooks
├── id_21_2025-10-18-19-31/       # Demo notebooks
├── jupyter-Notebook/             # Jupyter examples
│   └── Test-Test/                # RAG demo (OpenRouter + NagaAI)
├── requirements.txt              # Dependencies
├── pyproject.toml               # Project config
└── .env                         # Your API keys (create this)
```

## Technologies

- Python 3.12+
- LangChain (AI framework)
- OpenRouter (Multi-model API)
- NagaAI (Embeddings)
- FAISS (Vector database)
- HuggingFace (Embeddings)

## Usage Example

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    model="openai/gpt-4o-mini",
    temperature=0.7
)

response = llm.invoke("What is the capital of Thailand?")
print(response.content)
```

## Troubleshooting

**Missing module error:**
```bash
pip install -r requirements.txt
```

**Missing API key:**
- Create `.env` file in project root
- Add `OPENROUTER_API_KEY=your_key_here`

## Resources

- [LangChain Docs](https://docs.langchain.com/)
- [OpenRouter Docs](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)

## License

Educational purposes - feel free to use and learn!
