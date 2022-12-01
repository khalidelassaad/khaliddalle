import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def getUrlFromPrompt(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

def getUrlFromPromptAndInputAndMask(prompt, inputFilePath, maskFilePath):
    response = openai.Image.create_edit(
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

if __name__ == "__main__":
    getUrlFromPromptAndInputAndMask(
        "",
        "",
        ""
    )