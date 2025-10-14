"""PyCharm (With LangChain) — OpenRouter + Perplexity (เว็บเสิร์ชในตัว) — minimal"""

# ============================================================================
# IMPORTS
# ============================================================================
import os  # ตัวแปรสภาพแวดล้อม
from dotenv import load_dotenv  # โหลด .env
from langchain_openai import ChatOpenAI  # LangChain + OpenRouter
from langchain_core.prompts import ChatPromptTemplate  # message-style prompt

# ============================================================================
# ENVIRONMENT SETUP (module level, fail-fast)
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
    # โมเดล Perplexity (sonar) มีเว็บเสิร์ชในตัวบน OpenRouter
    llm = ChatOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        model="perplexity/sonar",
        temperature=0.3,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "คุณเป็นผู้สรุปข่าวแบบกระชับ ชัดเจน และเชื่อถือได้"),
        ("human", "สรุปข่าวดี ๆ วันที่ {date_text} สั้น ๆ 2–3 ประโยค"),
    ])

    date_text = "14 ตุลาคม 2025 (October 14, 2025)"
    resp = (prompt | llm).invoke({"date_text": date_text})

    print(f"📰 ข่าวดีวันนี้ ({date_text}):")
    print(resp.content)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
