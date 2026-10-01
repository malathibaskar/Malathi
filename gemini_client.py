from functools import lru_cache

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    MAX_OUTPUT_TOKENS,
    TEMPERATURE
)


class GeminiError(Exception):
    """
    Custom exception for Gemini-related errors.
    """
    pass


@lru_cache(maxsize=1)
def get_client():

    if not GEMINI_API_KEY:

        raise GeminiError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    return client


async def generate_text(prompt: str) -> str:

    try:

        client = get_client()

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=TEMPERATURE,
                max_output_tokens=MAX_OUTPUT_TOKENS
            )
        )

        text = getattr(
            response,
            "text",
            None
        )

        if not text:

            raise GeminiError(
                "Gemini returned an empty response."
            )

        return text.strip()

    except Exception as error:

        raise GeminiError(
            f"Gemini request failed: {error}"
        ) from error