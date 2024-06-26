import openai

import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
model = client.completions.create(
    model='gpt-3.5-turbo-instruct',
    # model='gpt-3.5-turbo',
    prompt='how do you say hello in hindi?  ',
)

print(model)

# Completion(id='cmpl-9dzVp9pKrEFfqAxkBABJ54o5TmgIR', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text='\n\nThe meaning of life is a question that has been pondered by humans for')], created=1719318273, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=16, prompt_tokens=7, total_tokens=23))