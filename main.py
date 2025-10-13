import os

from dotenv import load_dotenv

load_dotenv()

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Load API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")


def main():
    print("Hello from langchain-course!")
    print("OpenRouter Base URL:", OPENROUTER_BASE_URL)
    if API_KEY:
        print(
            "OpenRouter API Key:", "***" + API_KEY[-4:]
        )  # Hide most of the key for security
    else:
        print("OpenRouter API Key: Not found - please check your .env file")


if __name__ == "__main__":
    main()