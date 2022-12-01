import os
import openai
from dotenv import load_dotenv

from saveutil import openUrlAndSavePhoto

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
        image=open(inputFilePath, "rb"),
        mask=open(maskFilePath, "rb"),
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

if __name__ == "__main__":
    openUrlAndSavePhoto(
        getUrlFromPromptAndInputAndMask(            
            "A secret agent lounges on the couch smoking a cigar",
            "C:\\Users\\Khalid\\Desktop\\khaliddalle\\inputs\\original.png",
            "C:\\Users\\Khalid\\Desktop\\khaliddalle\\inputs\\mask.png"
        )
    )