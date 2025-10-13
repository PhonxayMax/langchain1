"""PyCharm (With LangChain) — OpenRouter minimal (fixed)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os # Importing os module to interact with the operating system
from dotenv import load_dotenv # Loads environment variables from.env file
from langchain_openai import ChatOpenAI # ใช้ LangChain แทน OpenAI โดยตรง

# ============================================================================
# ENVIRONMENT SETUP
# ============================================================================
# Load environment variables from .env file at module level (runs when file is imported/executed)
load_dotenv()

# ============================================================================
# CONFIGURATION VARIABLES
# ============================================================================
# Get the OpenRouter API key from environment variables
# This is loaded once when the module starts, not every time main() runs
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if not openrouter_api_key:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

# Get the OpenRouter base URL from environment variables  
# This tells the client where to send API requests (OpenRouter instead of OpenAI directly)
openrouter_base_url = os.getenv("OPENROUTER_BASE_URL")
if not openrouter_base_url:
    raise RuntimeError("Missing OPENROUTER_BASE_URL in .env")

# ============================================================================
# MAIN FUNCTION
# ============================================================================
def main():
    # Create a ChatOpenAI instance configured to use OpenRouter
    # base_url: Points to OpenRouter's API endpoint instead of OpenAI's
    # api_key: Your OpenRouter API key for authentication
    # model: The specific model you want to use (OpenRouter format)
    # temperature: Controls randomness (0 = deterministic, 1 = very random)
    llm = ChatOpenAI(
        api_key=openrouter_api_key,
        base_url=openrouter_base_url,  # Now using the variable, not the undefined constant
        model="openai/gpt-4o",   # OpenRouter model format: provider/model-name
        temperature=0.7,
    )
    
    # ────────────────────────────────────────────────────────────────────────
    # Execute AI Query
    # ────────────────────────────────────────────────────────────────────────
    resp = llm.invoke("What is the capital of Thailand?")
    print(resp.content)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
