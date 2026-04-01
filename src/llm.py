from openai import OpenAI
import os
from src.prompt import system_instruction
 
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],   # your OpenRouter key
    base_url="https://openrouter.ai/api/v1",   # <-- important
)
messages=[
            {"role": "system", "content": system_instruction},
        ]

def ask_order(messages, model = "gpt-3.5-turbo", temperature = 0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content
    