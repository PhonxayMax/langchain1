"""PyCharm (With LangChain) — OpenRouter minimal (ตามสไตล์ของเรา)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os  # ใช้งานตัวแปรสภาพแวดล้อม
from dotenv import load_dotenv  # โหลดค่าใน .env
from langchain_openai import ChatOpenAI  # ใช้ LangChain กับ OpenRouter
from langchain_core.prompts import ChatPromptTemplate  # ใช้ Prompt แบบแชต

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

    # prompt template: อธิบาย {topic} ให้เข้าใจง่ายใน {word} คำ
    prompt = ChatPromptTemplate.from_template(
        "อธิบายเกี่ยวกับ {topic} ให้เข้าใจง่ายใน {word} คำ"
    )

    # สร้าง chain และเรียกใช้งาน
    chain = prompt | llm
    response = chain.invoke({"topic": "ฟิสิกส์", "word": 5})
    print(response.content)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
