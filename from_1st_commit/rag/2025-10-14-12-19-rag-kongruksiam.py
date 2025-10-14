"""PyCharm (With LangChain) — RAG minimal
- LLM: OpenRouter (ChatOpenAI, openai/gpt-4o)
- Embedding: NagaAI (OpenAIEmbeddings, text-embedding-3-small)
"""

# ============================================================================
# IMPORTS
# ============================================================================
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# ============================================================================
# ENVIRONMENT SETUP (load once at module level, fail-fast)
# ============================================================================
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")
if not OPENROUTER_BASE_URL:
    raise RuntimeError("Missing OPENROUTER_BASE_URL in .env")

NAGA_API_KEY = os.getenv("NAGA_API_KEY")
NAGA_BASE_URL = os.getenv("NAGA_BASE_URL")
if not NAGA_API_KEY:
    raise RuntimeError("Missing NAGA_API_KEY in .env")
if not NAGA_BASE_URL:
    raise RuntimeError("Missing NAGA_BASE_URL in .env")

# ============================================================================
# MAIN
# ============================================================================
def main():
    # 1) โหลดเอกสาร
    loader = TextLoader("data.txt", encoding="utf-8")
    documents = loader.load()

    # 2) แบ่งข้อมูลเป็นชิ้นเล็ก (คงพารามิเตอร์ตามต้นฉบับ)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # 3) ฝั่งเวกเตอร์: ใช้ NagaAI embeddings
    embedding = OpenAIEmbeddings(
        api_key=NAGA_API_KEY,
        base_url=NAGA_BASE_URL,
        model="text-embedding-3-small",
    )

    # 4) เก็บลงเวกเตอร์สโตร์ (FAISS)
    vectorstore = FAISS.from_documents(chunks, embedding)

    # 5) ตัวดึงข้อมูล (Retriever)
    retriever = vectorstore.as_retriever()

    # 6) Prompt (ไทย) + LLM (OpenRouter)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "ใช้ข้อมูลจากเอกสารในการตอบคำถามให้สั้น กระชับ สุภาพ และเป็นกันเอง"),
        ("human", "คำถาม: {question}\nข้อมูลที่เกี่ยวข้อง:\n{context}")
    ])

    llm = ChatOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        model="openai/gpt-4o",
        temperature=0.7,
    )

    # 7) RAG Chain (retrieval → prompt → llm → parse เป็น str)
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # 8) ใช้งาน
    question = "มีสินค้าและบริการอะไรบ้าง"
    result = rag_chain.invoke(question)
    print(result)


# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
