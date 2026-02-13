
from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_structured_data(system_prompt: str, text: str):
    completion = client.chat.completions.create(
     model=MODEL_NAME,
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    content = completion.choices[0].message.content

    try:
        parsed = json.loads(content)
    except:
        raise ValueError("Invalid JSON returned by model")

    return parsed, completion.usage
