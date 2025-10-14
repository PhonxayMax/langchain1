"""OpenRouter (No LangChain) + Perplexity (มีเว็บเสิร์ชในตัว)"""

# ============================================================================
# IMPORTS
# ============================================================================
import os
from dotenv import load_dotenv
from openai import OpenAI

# ============================================================================
# ENVIRONMENT SETUP
# ============================================================================
load_dotenv()
key = os.getenv("OPENROUTER_API_KEY")
if not key: 
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

# ============================================================================
# MAIN
# ============================================================================
def main():
    client = OpenAI(api_key=key, base_url="https://openrouter.ai/api/v1")
    resp = client.chat.completions.create(
        model="perplexity/sonar",  # โมเดลนี้ค้นเว็บได้ในตัว
        messages=[{
            "role":"user",
            "content":"สรุปข่าวดี ๆ วันที่ 14 ตุลาคม 2025 (October 14, 2025) วันนี้สั้น ๆ 2-3 ประโยค"
        }],
    )
    print("📰 ข่าวดีวันนี้ (14 ตุลาคม 2025):")
    print(resp.choices[0].message.content)

# ============================================================================
# SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
