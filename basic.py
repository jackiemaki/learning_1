import google.generativeai as palm
import os

palm.configure(api_key=os.environ.get("GEMINI_API_KEY"))

my_prompt = "how old google is"

response = palm.generate_text(prompt=my_prompt)

print(response.result)