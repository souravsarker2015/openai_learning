import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

prompt = """
You are a chatbot that speaks like a toddler.

User: Hi, how are you?
Chatbot: I'm good
User: Tell me about your family
Chatbot: I have a mommy and a daddy and a baby sister and two kitties
User: What do you do for fun?
Chatbot: I like to play with my toys, color, go outside and explore, play with my kitties, read stories, and play games with my family.
User: That sounds like fun! What's your favorite game?
Chatbot:
"""

response = client.completions.create(
    model='gpt-3.5-turbo-instruct',
    # model='gpt-3.5-turbo',
    # prompt='give me the best movies of all time:  ',
    prompt=prompt,
    max_tokens=100,  # default 16
    # stop='4.'
    stop=["Chatbot:", "User:"]
)

print(response.choices[0].text)



# Completion(id='cmpl-9e05TXtfkOsyoZBF70WdZ25xB5bLj', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text="\n\nThat's a difficult question as it really depends on personal taste. However, here are some of the most highly acclaimed and influential movies of all time:\n\n1. The Godfather (1972)\n2. The Shawshank Redemption (1994)\n3. The Godfather: Part II (1974)\n4. Pulp Fiction (1994)\n5. The Dark Knight (2008)\n6. Schindler's List (1993)\n7. The Lord of the Rings:")], created=1719320483, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=100, prompt_tokens=10, total_tokens=110))
