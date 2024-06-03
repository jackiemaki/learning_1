import openai
from openai import OpenAI
import os

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

messages = []
messages.append({"role": "user", "content": "what programming language is the best?"})

try:
    response = client.chat.completions.create(messages = messages, 
                                            model = "gpt-3.5-turbo",
                                            n = 3,
                                            temperature = 0.9,
                                            max_tokens = 500,
                                            )

    print(response.choices[0].message.content)

except openai.AuthenticationError:
    print('no valid token / authentication error')
except openai.BadRequestError as e:
    print('invalid request')
    print(e)
