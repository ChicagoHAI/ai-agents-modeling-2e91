import os
import openai

if "OPENROUTER_API_KEY" in os.environ:
    openai.api_key = os.environ["OPENROUTER_API_KEY"]
    openai.api_base = "https://openrouter.ai/api/v1"
    print("Using OpenRouter")

try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
