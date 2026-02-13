
from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
model=MODEL_NAME,
messages=[
{
"role": "user",
"content": "Write a one-sentence bedtime story about a unicorn."
}
]
)

print(completion.choices[0].message.content)
