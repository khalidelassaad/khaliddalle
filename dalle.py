import os
import openai
import sys
import webbrowser
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def getImageUrl(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:])
    imageURL = getImageUrl(prompt)
    webbrowser.open(imageURL)
