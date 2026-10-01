from gemini_client import generate_text


async def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
You are EduGenie, a personalized educational
learning-path assistant.

Create a structured learning path for:

{topic}

The learner is starting at beginner level.

Organize the plan into:

1. Beginner
2. Intermediate
3. Advanced

For every stage provide:

- Topics to learn
- Important concepts
- Suggested timeline
- Practice activities
- Suggested resource types
- What the learner should be able to do afterward

Also include:

- A small final project
- Revision strategy
- Practice strategy

Make the plan realistic and easy to follow.
"""

    return await generate_text(
        prompt
    )