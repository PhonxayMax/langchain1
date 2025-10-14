"""PyCharm (With LangChain) — NagaAI Embeddings (minimal, strict)"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# load env & fail-fast
load_dotenv()
NAGA_API_KEY = os.getenv("NAGA_API_KEY")
if not NAGA_API_KEY:
    raise RuntimeError("Missing NAGA_API_KEY in .env")
NAGA_BASE_URL = os.getenv("NAGA_BASE_URL")
if not NAGA_BASE_URL:
    raise RuntimeError("Missing NAGA_BASE_URL in .env")

def main():
    embeddings = OpenAIEmbeddings(
        api_key=NAGA_API_KEY,
        base_url=NAGA_BASE_URL,
        model="text-embedding-3-small",
    )
    texts = ["The food was delicious!", "Service could be faster."]
    vectors = embeddings.embed_documents(texts)  # -> List[List[float]]
    print(vectors)

if __name__ == "__main__":
    main()
