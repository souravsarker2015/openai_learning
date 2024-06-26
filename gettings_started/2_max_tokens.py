import openai

import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
model = client.completions.create(
    model='gpt-3.5-turbo-instruct',
    # model='gpt-3.5-turbo',
    prompt='top 10 populated cities in the world :  ',
    max_tokens=100  # default 16
)

print(model)

# Completion(id='cmpl-9e00NuN63gzAHgBhM9ZxRr9wqHnfY', choices=[CompletionChoice(finish_reason='stop', index=0, logprobs=None, text='\n\n1. Tokyo, Japan \n2. Delhi, India \n3. Shanghai, China \n4. Mumbai, India \n5. Beijing, China \n6. Karachi, Pakistan \n7. Istanbul, Turkey \n8. Dhaka, Bangladesh \n9. Tokyo, Japan \n10. Mexico City, Mexico')], created=1719320167, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=62, prompt_tokens=10, total_tokens=72))
