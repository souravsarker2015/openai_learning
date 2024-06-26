import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.completions.create(
    model='gpt-3.5-turbo-instruct',
    prompt='Q: What is the tallest building in the world?',
    max_tokens=100,  # default 16
    # n=3
    echo=True
)

print(response)
print(response.choices[0].text)
