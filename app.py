import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt="a robot seated by a river, painting a beautiful bridge on a canvas",
    n=1,
    size="512x512"
)
image_url = response['data'][0]['url']
print(response)
