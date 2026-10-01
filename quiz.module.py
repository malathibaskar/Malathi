import json
import re

from gemini_client import generate_text


def clean_json_block(
    text: str
) -> str:

    text = text.strip()

    # Remove markdown JSON blocks
    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    # Find JSON array
    start = text.find("[")

    end = text.rfind("]")

    if start == -1 or end == -1:

        raise ValueError(
            "Could not find JSON array in Gemini response."
        )

    return text[
        start:end + 1
    ]


async def generate_quiz(
    passage: str
):

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly THREE multiple-choice questions
from the provided educational text.

Each question must have exactly FOUR options.

Return ONLY valid JSON.

Use exactly this structure:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Correct option",
    "explanation": "Short explanation"
  }}
]

Important rules:

1. Exactly 3 questions.
2. Exactly 4 options per question.
3. The correct_answer must exactly match one option.
4. Questions must be based only on the supplied text.
5. Make incorrect options plausible.
6. Do not include markdown.
7. Do not include anything outside the JSON.

Educational text:

{passage}
"""

    response = await generate_text(
        prompt
    )

    try:

        cleaned = clean_json_block(
            response
        )

        quiz = json.loads(
            cleaned
        )

        if not isinstance(
            quiz,
            list
        ):

            raise ValueError(
                "Quiz response is not a list."
            )

        if len(quiz) != 3:

            raise ValueError(
                "Quiz must contain exactly 3 questions."
            )

        for question in quiz:

            if "question" not in question:
                raise ValueError(
                    "Question field missing."
                )

            if "options" not in question:
                raise ValueError(
                    "Options field missing."
                )

            if len(
                question["options"]
            ) != 4:

                raise ValueError(
                    "Each question must have 4 options."
                )

            if question[
                "correct_answer"
            ] not in question[
                "options"
            ]:

                raise ValueError(
                    "Correct answer must match an option."
                )

        return quiz

    except Exception as error:

        raise ValueError(
            f"Quiz generation/parsing failed: {error}"
        ) from error