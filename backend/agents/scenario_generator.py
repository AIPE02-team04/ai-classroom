"""
Agent Layer - Custom Scenario Generator
用 GPT-4o mini 根據用戶描述自動生成 student_prompt 與 initial_emotions。
"""
import os
import json
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SEL_CATEGORIES = ["自我覺察", "自我管理", "社會覺察", "關係技能", "負責任的決策"]

SYSTEM_PROMPT = """你是一位專業的台灣國中班級情境設計師。
根據老師提供的情境描述，你需要輸出：
1. student_prompt：第一人稱視角（學生的內心獨白），描述學生當下身處的情況、感受與想法。格式參考：「你是正在上XXX課的學生。剛才...，現在老師走過來。你感到...」
2. initial_emotions：9種情緒的初始強度（0.0–1.0），必須符合情境氛圍。
   - HAPPY, SAD, ANGRY, SURPRISED, ANXIOUS, FRUSTRATED, CONFIDENT, CURIOUS, NEUTRAL
3. sel_category：從以下選一個最符合的：自我覺察、自我管理、社會覺察、關係技能、負責任的決策
4. short_desc：20字以內的情境摘要
5. emoji：一個最能代表此情境的 emoji

注意事項：
- student_prompt 必須是學校班級場景，即使老師描述的是其他場景
- 情緒分數的總和不限，但需合理反映情境（如衝突情境 ANGRY + FRUSTRATED 應偏高）
- 輸出純 JSON，不加任何說明文字"""


async def generate_scenario_content(title: str, description: str) -> dict:
    """
    根據標題與描述，用 GPT-4o mini 生成 student_prompt、initial_emotions 等欄位。
    回傳 dict，失敗時 raise Exception。
    """
    user_message = f"情境標題：{title}\n情境描述：{description}"

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)

    # 驗證必要欄位存在
    required = {"student_prompt", "initial_emotions", "sel_category", "short_desc", "emoji"}
    missing = required - data.keys()
    if missing:
        raise ValueError(f"LLM 輸出缺少欄位：{missing}")

    # 驗證情緒欄位完整
    emotion_keys = {"HAPPY", "SAD", "ANGRY", "SURPRISED", "ANXIOUS", "FRUSTRATED", "CONFIDENT", "CURIOUS", "NEUTRAL"}
    missing_emotions = emotion_keys - set(data["initial_emotions"].keys())
    if missing_emotions:
        raise ValueError(f"initial_emotions 缺少：{missing_emotions}")

    # sel_category 限定範圍
    if data["sel_category"] not in SEL_CATEGORIES:
        data["sel_category"] = "關係技能"  # fallback

    return {
        "student_prompt": data["student_prompt"],
        "initial_emotions": {k: float(v) for k, v in data["initial_emotions"].items()},
        "sel_category": data["sel_category"],
        "short_desc": data["short_desc"][:200],
        "emoji": data["emoji"],
    }
