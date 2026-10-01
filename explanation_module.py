from config import (
    USE_LOCAL_EXPLANATION,
    LOCAL_EXPLANATION_MODEL
)

from gemini_client import generate_text


def local_explanation(
    topic: str
) -> str:

    from transformers import pipeline

    generator = pipeline(
        "text2text-generation",
        model=LOCAL_EXPLANATION_MODEL
    )

    prompt = f"""
Explain this educational topic
for a beginner using very simple language.

Topic:

{topic}
"""

    result = generator(
        prompt,
        max_new_tokens=250
    )

    return result[0]["generated_text"].strip()


async def explain_concept(
    topic: str
) -> str:

    # Optional local model
    if USE_LOCAL_EXPLANATION:

        try:

            return local_explanation(
                topic
            )

        except Exception:

            # If local model fails,
            # use Gemini instead.
            pass


    # Gemini explanation
    prompt = f"""
You are EduGenie, a patient educational tutor.

Explain the following topic to
a beginner.

Requirements:

- Use simple language.
- Break complex ideas into small parts.
- Define difficult terms.
- Give a simple example.
- Use headings when useful.
- Keep the explanation clear and concise.
- Do not assume advanced knowledge.

Topic:

{topic}
"""

    return await generate_text(
        prompt
    )