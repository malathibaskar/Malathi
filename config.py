import os

from dotenv import load_dotenv


# Load .env file
load_dotenv()


# -----------------------------
# Gemini Configuration
# -----------------------------

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
).strip()


GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
).strip()


# -----------------------------
# Local Explanation Model
# -----------------------------

LOCAL_EXPLANATION_MODEL = os.getenv(
    "LOCAL_EXPLANATION_MODEL",
    "MBZUAI/LaMini-Flan-T5-783M"
).strip()


USE_LOCAL_EXPLANATION = (
    os.getenv(
        "USE_LOCAL_EXPLANATION",
        "false"
    ).lower()
    == "true"
)


# -----------------------------
# Generation Settings
# -----------------------------

MAX_OUTPUT_TOKENS = int(
    os.getenv(
        "MAX_OUTPUT_TOKENS",
        "1200"
    )
)


TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0.4"
    )
)