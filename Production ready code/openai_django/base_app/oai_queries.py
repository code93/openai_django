# import settings
from django.conf import settings
import os
import openai
from openai import OpenAI


# OpenAI API Key
if settings.OPENAI_API_KEY:
    client = OpenAI(api_key = settings.OPENAI_API_KEY)
else:
    raise Exception('OpenAI API Key not found')


def get_completion(prompt):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt }]
    )

    return response.choices[0].message.content.strip()
