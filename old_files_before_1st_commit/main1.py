"""PyCharm (With LangChain) — OpenRouter minimal: generate marketing slogans"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def main():
    load_dotenv()
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

    llm = ChatOpenAI(api_key=key, base_url="https://openrouter.ai/api/v1",
                     model="openai/gpt-4o", temperature=0.7)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a world-class copywriter. Be punchy and concise."),
        ("human", "Generate ONE catchy marketing slogan for {product} highlighting {feature}. "
                  "Return a single line only.")
    ])
    chain = prompt | llm

    # Original single example
    first = {"product": "LangChain", "feature": "AI orchestration"}
    print("Generated slogan:", chain.invoke(first).content)

    # Original examples list
    examples = [
        {"product": "Smartphone", "feature": "camera quality"},
        {"product": "Electric Car", "feature": "eco-friendly"},
        {"product": "AI Assistant", "feature": "natural conversation"},
    ]
    for ex in examples:
        print("•", chain.invoke(ex).content)

    with open("basic-templates.txt", "w", encoding="utf-8") as f:
        f.write("BASIC_TEMPLATES_COMPLETE")

if __name__ == "__main__":
    main()
