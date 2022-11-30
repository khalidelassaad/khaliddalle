import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-002",
    prompt="PROMPT GOES HERE",
    temperature=0.6,
)

result = response.choices[0].text
print(result)
