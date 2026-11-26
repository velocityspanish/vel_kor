"""VELOCITY KOREAN - storybook production interface.

The live bot builds one storybook reel per run, rotates world / palette / cast,
and publishes the result with the uploaders in ``upload/``.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = Path(os.getenv("VEL_OUTPUT_DIR", str(BASE_DIR / "output")))
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"
SCENE_DIRS = {
    "poster": SCENE_DIR,
    "storybook": BASE_DIR / "scene_storybook",
}


def scene_dir(style: str) -> Path:
    return SCENE_DIRS.get(style, SCENE_DIR)

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY KOREAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "KOREAN"
HANDLE = "@velocitykorean"
MASCOT_NAME = "Velo"
WEBSITE = "https://velocitykorean.com"
WEBSITE_LABEL = "velocitykorean.com"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'ko',
 'name': 'Korean',
 'native_name': '한국어',
 'history_key': 'korean',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'ko-KR-SunHiNeural',
 'native_fallback_voice': 'ko-KR-InJoonNeural',
 'native_engine': 'edge',
 'native_lang_code': 'ko',
 'english_rate': '-2%',
 'native_rate': '-6%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': '한국어',
 'translit_label': 'ROMANIZED',
 'greeting': '안녕하세요!',
 'encouragement': '훌륭해요!',
 'rtl': False,
 'char_tiles': False,
 'script_font': 'NotoSansKR-Variable.ttf',
 'tile_scale': 1.16}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)
#
# Hard rule for this experiment: the finished reel must be < 60 s.
# Everything below is a budget, not a suggestion.

MAX_REEL_DURATION = 59.4
TARGET_REEL_DURATION = 56.0
MIN_PHRASES = 3
MAX_PHRASES = 5

INTRO_DURATION = 2.4
OUTRO_DURATION = 4.0

PACE = {
    "tight": {
        "en_card_in": 0.28,
        "gap_en_native": 0.30,
        "native_card_lead": 0.15,
        "gap_before_echo": 0.45,
        "tail_hold": 0.50,
    },
    "standard": {
        "en_card_in": 0.38,
        "gap_en_native": 0.42,
        "native_card_lead": 0.20,
        "gap_before_echo": 0.65,
        "tail_hold": 0.70,
    },
    "story": {
        "en_card_in": 0.50,
        "gap_en_native": 0.55,
        "native_card_lead": 0.30,
        "gap_before_echo": 0.80,
        "tail_hold": 0.95,
    },
}

# ---------------------------------------------------------------- audio

# Earphone-friendly SFX: softer timbres, lower level, gentle top-end roll-off.
SFX_MASTER = 0.55
SFX_LOWPASS_HZ = 6500
MASTER_GAIN = 0.82

# ---------------------------------------------------------------- colour worlds
#
# One bold colour world per phrase. The video rotates through 4-5 of these,
# and the experiment loop can promote whichever worlds retain best.

THEMES = {
    "citrus": {
        "name": "Citrus Pop",
        "bg": "#FF6B35", "bg2": "#FFC800", "card": "#FFF8EC", "ink": "#2B1B00",
        "colors": ["#FFC800", "#FF3D7F", "#00B894", "#7C5CFF", "#FF6B35"],
    },
    "berry": {
        "name": "Berry Fizz",
        "bg": "#E84393", "bg2": "#FF8FC7", "card": "#FFF4F8", "ink": "#3A0B22",
        "colors": ["#FFC800", "#00C2A8", "#7C5CFF", "#FF6B35", "#E84393"],
    },
    "ocean": {
        "name": "Ocean Ink",
        "bg": "#0096C7", "bg2": "#48CAE4", "card": "#F2FBFF", "ink": "#04283A",
        "colors": ["#FFC800", "#FF6B35", "#90E0EF", "#FF3D7F", "#0096C7"],
    },
    "forest": {
        "name": "Forest Lime",
        "bg": "#2E9E4F", "bg2": "#A7E86B", "card": "#F4FBEC", "ink": "#10280A",
        "colors": ["#FFC800", "#FF6B35", "#A560E8", "#00C2A8", "#2E9E4F"],
    },
    "grape": {
        "name": "Grape Tape",
        "bg": "#7B2CBF", "bg2": "#C77DFF", "card": "#F8F3FF", "ink": "#1E0B3A",
        "colors": ["#FFC800", "#FF6B35", "#00E5FF", "#FF3D7F", "#7B2CBF"],
    },
    "sunset": {
        "name": "Sunset Heat",
        "bg": "#FF4D00", "bg2": "#FFB703", "card": "#FFF3E8", "ink": "#3A1400",
        "colors": ["#FFB703", "#00C2A8", "#FF3D7F", "#7C5CFF", "#FF4D00"],
    },
    "lagoon": {
        "name": "Lagoon",
        "bg": "#00A889", "bg2": "#7BF1D8", "card": "#EDFFFB", "ink": "#003B36",
        "colors": ["#FFC800", "#FF6B35", "#FF3D7F", "#7C5CFF", "#00A889"],
    },
    "cherry": {
        "name": "Cherry Soda",
        "bg": "#E63946", "bg2": "#FFB3C1", "card": "#FFF2F2", "ink": "#3B0505",
        "colors": ["#FFC800", "#00C2A8", "#7C5CFF", "#FF8C42", "#E63946"],
    },
    "cobalt": {
        "name": "Cobalt",
        "bg": "#2563EB", "bg2": "#60A5FA", "card": "#F2F6FF", "ink": "#071B4A",
        "colors": ["#FFC800", "#FF6B35", "#00C2A8", "#FF3D7F", "#2563EB"],
    },
    "mango": {
        "name": "Mango",
        "bg": "#F5A700", "bg2": "#FFD166", "card": "#FFFBEC", "ink": "#3B2A00",
        "colors": ["#FF4D00", "#00A889", "#7C5CFF", "#FF3D7F", "#F5A700"],
    },
    "rose": {
        "name": "Rose",
        "bg": "#D6336C", "bg2": "#FFA8C5", "card": "#FFF2F7", "ink": "#3A0418",
        "colors": ["#FFC800", "#00C2A8", "#7C5CFF", "#FF8C42", "#D6336C"],
    },
    "teal": {
        "name": "Deep Teal",
        "bg": "#0F766E", "bg2": "#5EEAD4", "card": "#F0FDFA", "ink": "#022C2A",
        "colors": ["#FFC800", "#FF6B35", "#FF3D7F", "#A78BFA", "#0F766E"],
    },
    "duo": {
        "name": "Duo Green",
        "bg": "#58CC02", "bg2": "#8FE63D", "card": "#FFFDF6", "ink": "#263A0A",
        "colors": ["#FFC800", "#1CB0F6", "#FF4B4B", "#CE82FF", "#FF9600"],
    },
}

# Five full-bleed background worlds per theme. Each phrase gets the next one,
# so a 4-phrase video shows 4 different colour worlds before the outro.
THEME_WORLDS = {
    "citrus": ["#FF6B35", "#FFC800", "#FF3D7F", "#00B894", "#2563EB"],
    "berry":  ["#E84393", "#7B2CBF", "#FF6B35", "#00A889", "#0096C7"],
    "ocean":  ["#0096C7", "#2563EB", "#00A889", "#7B2CBF", "#FF6B35"],
    "forest": ["#2E9E4F", "#0F766E", "#7B2CBF", "#FF6B35", "#F5A700"],
    "grape":  ["#7B2CBF", "#E84393", "#2563EB", "#0F766E", "#00A889"],
    "sunset": ["#FF4D00", "#F5A700", "#E63946", "#7B2CBF", "#0096C7"],
    "lagoon": ["#00A889", "#0096C7", "#2E9E4F", "#7B2CBF", "#FF4D00"],
    "cherry": ["#E63946", "#D6336C", "#F5A700", "#7B2CBF", "#2563EB"],
    "cobalt": ["#2563EB", "#7B2CBF", "#0096C7", "#0F766E", "#E84393"],
    "mango":  ["#F5A700", "#FF4D00", "#FF6B35", "#00A889", "#7B2CBF"],
    "rose":   ["#D6336C", "#E84393", "#7B2CBF", "#E63946", "#00A889"],
    "teal":   ["#0F766E", "#0096C7", "#2E9E4F", "#7B2CBF", "#F5A700"],
    "duo":    ["#58CC02", "#8FE63D", "#1CB0F6", "#FFC800", "#FF8FA3"],
}
for _theme_id, _worlds in THEME_WORLDS.items():
    THEMES[_theme_id]["worlds"] = _worlds

# ---------------------------------------------------------------- recipes (experiment arms)
#
# A recipe is everything the loop is allowed to change without editing code.
# Keep this list small enough that each arm can collect a real sample.

RECIPES = [
    {"id": "citrus-4-tight",  "theme": "citrus", "phrases": 4, "pace": "tight",    "music": "bright", "hook": "count"},
    {"id": "ocean-4-tight",   "theme": "ocean",  "phrases": 4, "pace": "tight",    "music": "bright", "hook": "count"},
    {"id": "grape-4-tight",   "theme": "grape",  "phrases": 4, "pace": "tight",    "music": "chill",  "hook": "question"},
    {"id": "sunset-5-tight",  "theme": "sunset", "phrases": 5, "pace": "tight",    "music": "bright", "hook": "count"},
    {"id": "berry-4-tight",   "theme": "berry",  "phrases": 4, "pace": "tight",    "music": "bright", "hook": "number"},
    {"id": "forest-5-tight",  "theme": "forest", "phrases": 5, "pace": "tight",    "music": "chill",  "hook": "question"},
    {"id": "cherry-4-standard", "theme": "cherry", "phrases": 4, "pace": "standard", "music": "bright", "hook": "number"},
    {"id": "mango-4-tight",   "theme": "mango",  "phrases": 4, "pace": "tight",    "music": "chill",  "hook": "count"},
    {"id": "duo-4-tight",     "theme": "duo",    "phrases": 4, "pace": "tight",    "music": "bright", "hook": "count"},
    {
        "id": "storybook-3", "theme": "duo", "phrases": 3, "pace": "story", "music": "chill",
        "hook": "count", "style": "storybook", "intro": 3.0, "outro": 4.8,
    },
]

RECIPE_BY_ID = {r["id"]: r for r in RECIPES}

HOOKS = {
    "count":    "{n} PHRASES · UNDER 60s",
    "question": "CAN YOU SAY IT?",
    "number":   "LET'S GO · {n} PHRASES",
}

# ---------------------------------------------------------------- categories

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ('Greetings', '인사', 'hand', '#1CB0F6'),
    ('Basic Phrases', '기본 표현', 'chat', '#58CC02'),
    ('Common Expressions', '자주 쓰는 말', 'chat', '#1CB0F6'),
    ('Travel', '여행', 'plane', '#1CB0F6'),
    ('Restaurant', '식당', 'fork', '#FF7A00'),
    ('Shopping', '쇼핑', 'bag', '#E056A0'),
    ('Emergency', '긴급', 'siren', '#FF4B4B'),
    ('Family Terms', '가족 호칭', 'heart', '#E056A0'),
    ('Numbers', '숫자', 'hash', '#A560E8'),
    ('Time', '시간', 'clock', '#00A889'),
    ('Motivation', '동기 부여', 'rocket', '#A560E8'),
    ('Love', '사랑', 'heart', '#FF4B4B'),
    ('Success', '성공', 'trophy', '#F5A700'),
    ('Wisdom', '지혜', 'book', '#A560E8'),
    ('Happiness', '행복', 'smile', '#F5A700'),
    ('Self Improvement', '자기 계발', 'leaf', '#58CC02'),
    ('Gratitude', '감사', 'heart', '#FF7A00'),
    ('Friendship', '우정', 'users', '#00A889'),
    ('Hope', '희망', 'sun', '#FF7A00'),
    ('Creativity', '창의력', 'palette', '#E056A0'),
    ('Inner Peace', '마음의 평화', 'lotus', '#00A889'),
    ('Confidence', '자신감', 'shield', '#1CB0F6'),
    ('Perseverance', '인내심', 'mountain', '#FF7A00'),
    ('Inspiration', '영감', 'sparkles', '#A560E8'),
    ('Positive Life', '긍정적 삶', 'sun', '#58CC02'),
    ('Courage', '용기', 'shield', '#FF4B4B'),
    ('Kindness', '친절', 'heart', '#E056A0'),
    ('Patience', '끈기', 'hourglass', '#00A889'),
    ('Forgiveness', '용서', 'hands', '#FF7A00'),
    ('Strength', '힘', 'dumbbell', '#FF4B4B'),
    ('Joy', '기쁨', 'smile', '#F5A700'),
    ('Balance', '균형', 'scale', '#00A889'),
    ('Growth', '성장', 'sprout', '#58CC02'),
    ('Purpose', '목표', 'target', '#A560E8'),
    ('Mindfulness', '마음 챙김', 'lotus', '#00A889'),
    ('Daily Routine', '일상', 'calendar', '#1CB0F6'),
    ('Weather', '날씨', 'cloud', '#1CB0F6'),
    ('Feelings', '감정', 'smile', '#E056A0'),
    ('Food', '음식', 'fork', '#FF7A00'),
    ('Health', '건강', 'heart', '#58CC02'),
    ('Work', '일', 'briefcase', '#1CB0F6'),
    ('Technology', '기술', 'chip', '#A560E8'),
    ('Nature', '자연', 'leaf', '#58CC02'),
    ('Animals', '동물', 'paw', '#FF7A00'),
    ('Colors', '색깔', 'palette', '#E056A0'),
    ('Directions', '방향', 'compass', '#1CB0F6'),
    ('Body Parts', '신체 부위', 'hand', '#00A889'),
    ('Clothes', '옷', 'shirt', '#E056A0'),
    ('Music', '음악', 'music', '#A560E8'),
    ('Sports', '스포츠', 'ball', '#FF7A00'),
    ('Holidays', '명절', 'gift', '#FF4B4B'),
    ('Education', '교육', 'book', '#1CB0F6'),
    ('Culture', '문화', 'globe', '#00A889'),
    ('Finance', '재정', 'coin', '#58CC02'),
    ('Relationships', '관계', 'users', '#E056A0'),
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
    "#languagetips"
]
# ==== HASHTAGS END ====
