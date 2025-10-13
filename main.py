"""OpenRouter + LangChain (minimal)"""
import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def main():
    """
    Main function to run the LangChain example.
    """
    load_dotenv()
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

    llm = ChatOpenAI(
        api_key=key,
        base_url="https://openrouter.ai/api/v1",
        model="openai/gpt-4o",
        temperature=0.7,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Think step by step when asked."),
            ("human", "Question: {q}\nAnswer: Let's think step by step."),
        ]
    )

    chain = prompt | llm

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
    response = chain.invoke({"q": question})

    print(response.content)


if __name__ == "__main__":
    main()