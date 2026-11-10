"""VELOCITY KOREAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY KOREAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "KOREAN"
HANDLE = "@velocitykorean"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "ko",
    "name": "Korean",
    "native_name": "한국어",
    "history_key": "korean",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "ko-KR-SunHiNeural",
    "native_fallback_voice": "ko-KR-InJoonNeural",
    "native_engine": "edge",
    "native_lang_code": "ko",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "한국어",
    "translit_label": "ROMANIZED",
    "greeting": "안녕하세요!",
    "encouragement": "훌륭해요!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "NotoSansKR-Bold.ttf",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "인사말", "hand", "#1CB0F6"),
    ("Basic Phrases", "기본 표현", "chat", "#58CC02"),
    ("Common Expressions", "일반 표현", "chat", "#1CB0F6"),
    ("Travel", "여행", "plane", "#1CB0F6"),
    ("Restaurant", "식당", "fork", "#FF7A00"),
    ("Shopping", "쇼핑", "bag", "#E056A0"),
    ("Emergency", "비상", "siren", "#FF4B4B"),
    ("Family Terms", "가족 용어", "heart", "#E056A0"),
    ("Numbers", "숫자", "hash", "#A560E8"),
    ("Time", "시간", "clock", "#00A889"),
    ("Motivation", "동기부여", "rocket", "#A560E8"),
    ("Love", "사랑", "heart", "#FF4B4B"),
    ("Success", "성공", "trophy", "#F5A700"),
    ("Wisdom", "지혜", "book", "#A560E8"),
    ("Happiness", "행복", "smile", "#F5A700"),
    ("Self Improvement", "자기계발", "leaf", "#58CC02"),
    ("Gratitude", "감사", "heart", "#FF7A00"),
    ("Friendship", "우정", "users", "#00A889"),
    ("Hope", "희망", "sun", "#FF7A00"),
    ("Creativity", "창의성", "palette", "#E056A0"),
    ("Inner Peace", "내면의 평화", "lotus", "#00A889"),
    ("Confidence", "자신감", "shield", "#1CB0F6"),
    ("Perseverance", "인내심", "mountain", "#FF7A00"),
    ("Inspiration", "영감", "sparkles", "#A560E8"),
    ("Positive Life", "긍정적인 삶", "sun", "#58CC02"),
    ("Courage", "용기", "shield", "#FF4B4B"),
    ("Kindness", "친절", "heart", "#E056A0"),
    ("Patience", "인내", "hourglass", "#00A889"),
    ("Forgiveness", "용서", "hands", "#FF7A00"),
    ("Strength", "힘", "dumbbell", "#FF4B4B"),
    ("Joy", "기쁨", "smile", "#F5A700"),
    ("Balance", "균형", "scale", "#00A889"),
    ("Growth", "성장", "sprout", "#58CC02"),
    ("Purpose", "목적", "target", "#A560E8"),
    ("Mindfulness", "마음챙김", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnkorean",
    "#koreanlessons",
    "#koreanforbeginners",
    "#languagelearning",
    "#koreanvocabulary",
    "#velocitykorean",
    "#dailykorean",
    "#korean",
    "#learnlanguages",
    "#speakkorean",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
