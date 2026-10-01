from gemini_client import generate_text


async def summarize_text(
    text: str
) -> str:

    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following educational passage.

Requirements:

1. Keep the important information.
2. Remove unnecessary repetition.
3. Use simple language.
4. Make it useful for exam revision.
5. Keep important definitions and relationships.
6. Do not add information that is not present.
7. Use bullet points when helpful.

Educational Passage:

{text}
"""

    return await generate_text(
        prompt
    )