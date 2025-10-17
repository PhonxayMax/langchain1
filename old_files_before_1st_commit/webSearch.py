"""PyCharm (With LangChain) — OpenRouter + Serper (ultra-minimal, with your comment style)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os, requests  # เรียก Serper API แบบตรง + จัดการตัวแปรสภาพแวดล้อม
from dotenv import load_dotenv  # โหลดค่าจากไฟล์ .env
from langchain_openai import ChatOpenAI  # ใช้ LangChain กับ OpenRouter
from langchain_core.prompts import ChatPromptTemplate  # สร้าง prompt แบบข้อความหลายส่วน (messages)

# ============================================================================
# ENVIRONMENT SETUP (load once at module level, fail-fast)
# ============================================================================
load_dotenv()  # โหลดค่า .env ทันทีเมื่อโมดูลถูกรัน/นำเข้า

# ดึงค่าที่จำเป็นจาก environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# ตรวจสอบค่าที่จำเป็น หากขาดให้หยุดทันที (fail-fast)
if not OPENROUTER_API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")
if not OPENROUTER_BASE_URL:
    raise RuntimeError("Missing OPENROUTER_BASE_URL in .env")
if not SERPER_API_KEY:
    raise RuntimeError("Missing SERPER_API_KEY in .env")

# ============================================================================
# MAIN FUNCTION
# ============================================================================
def main():
    # ------------------------------------------------------------------------
    # 1) ค้นเว็บด้วย Serper (minimally): รับผลลัพธ์ 3 รายการแรก (title + snippet)
    # ------------------------------------------------------------------------
    resp = requests.post(
        "https://google.serper.dev/search",
        headers={"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"},
        json={"q": "Olivia Wilde current boyfriend age", "num": 5, "gl": "us", "hl": "en"},
        timeout=20,
    ).json()
    hits = (resp.get("news") or resp.get("organic") or [])[:3]
    corpus = "\n".join(
        f"- {h.get('title','').strip()}: {h.get('snippet') or h.get('description','')}"
        for h in hits
        if (h.get("title") or h.get("snippet") or h.get("description"))
    ) or "No results"

    # ------------------------------------------------------------------------
    # 2) สร้างโมเดล LLM (OpenRouter) ตามสไตล์เรา: model=openai/gpt-4o, temp=0.2
    # ------------------------------------------------------------------------
    llm = ChatOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        model="openai/gpt-4o",
        temperature=0.2,
    )

    # ------------------------------------------------------------------------
    # 3) Prompt แบบ messages (สั้น กระชับ): สกัดชื่อ + อายุ และคำนวณ age**0.23
    # ------------------------------------------------------------------------
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer concisely."),
        ("human",
         "From the snippets, identify Olivia Wilde's current boyfriend and his current age, "
         "then compute age**0.23. Reply as:\n"
         "Name: <name>\nAge: <age>\nAge**0.23: <value>\n\nSnippets:\n{corpus}")
    ])

    # เรียก chain แบบสั้น: prompt | llm แล้วพิมพ์ผล
    result = (prompt | llm).invoke({"corpus": corpus})
    print(result.content)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
