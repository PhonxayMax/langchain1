"""PyCharm (With LangChain) — OpenRouter minimal + StrOutputParser (ตามสไตล์เรา)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os  # ใช้งานตัวแปรสภาพแวดล้อม
from dotenv import load_dotenv  # โหลดค่าใน .env
from langchain_openai import ChatOpenAI  # LangChain + OpenRouter
from langchain_core.prompts import ChatPromptTemplate  # message-based prompt
from langchain_core.output_parsers import StrOutputParser  # << เพิ่ม Output Parser แบบข้อความ >>

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

    # prompt แบบ "messages" + ตัวแปร
    prompt = ChatPromptTemplate.from_messages([
        ("system", "คุณเป็น {expertise}"),
        ("human", "แนะนำเมนู {menu} จำนวน {amount} รายการ พร้อมคำอธิบายสั้น ๆ")
    ])

    # Output Parser -> คืนค่าเป็นสตริงตรง ๆ (ไม่ต้อง .content)
    parser = StrOutputParser()

    # สร้าง chain และเรียกใช้
    chain = prompt | llm | parser
    response = chain.invoke({
        "expertise": "เชฟอาหารไทย",
        "menu": "อาหารเหนือ",
        "amount": 5
    })
    print(response)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
