import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)
print(os.getenv("OPENAI_API_KEY"))
#openai.api_key = os.getenv("OPENAI_API_KEY")

question = input("What is your question for ChatGPT?")
response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[
        { "role": "system", "content": "You are a chatbot" },
        { "role": "user", "content": f"{question}" }
    ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(f"We asked ChatGPT: {question}; and the response was:")
print(result)