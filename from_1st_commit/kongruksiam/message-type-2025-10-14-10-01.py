"""PyCharm (With LangChain) — OpenRouter minimal (message-style, ตามสไตล์เรา)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os  # ใช้งานตัวแปรสภาพแวดล้อม
from dotenv import load_dotenv  # โหลดค่าใน .env
from langchain_openai import ChatOpenAI  # LangChain + OpenRouter
from langchain_core.prompts import ChatPromptTemplate  # message-based prompt

# ============================================================================
# ENVIRONMENT SETUP (load once at module level)
# ============================================================================
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")
if not OPENROUTER_BASE_URL:
    raise RuntimeError("Missing OPENROUTER_BASE_URL in .env")

# ============================================================================
# MAIN
# ============================================================================
def main():
    # สร้างโมเดล (OpenRouter format)
    llm = ChatOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        model="openai/gpt-4o",
        temperature=0.7,
    )

    # prompt แบบ "messages" มีตัวแปร expertise, topic, word
    prompt = ChatPromptTemplate.from_messages([
        ("system", "คุณเป็น {expertise}"),
        ("human", "อธิบายเกี่ยวกับ {topic} ให้เข้าใจง่ายใน {word} ประโยค"),
    ])

    # สร้าง chain แล้วเรียกใช้
    chain = prompt | llm
    response = chain.invoke({
        "expertise": "นักจิตวิทยา",
        "topic": "โรคซึมเศร้า",
        "word": 2
    })
    print(response.content)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
