import os
import openai
from dotenv import load_dotenv

from saveutil import openUrlAndSavePhoto

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def getUrlListFromPrompt(prompt, count):
    imageURLs = []
    response = openai.Image.create(
        prompt=prompt,
        n=count,
        size="1024x1024"
    )
    for urlObject in response['data']:
        imageURLs.append(urlObject['url'])
    return imageURLs


def getUrlFromPromptAndInputAndMask(prompt, inputFilePath, maskFilePath):
    response = openai.Image.create_edit(
        image=open(inputFilePath, "rb"),
        mask=open(maskFilePath, "rb"),
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url


def getUrlFromInput(inputFilePath):
    response = openai.Image.create_variation(
        image=open(inputFilePath, "rb"),
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url


if __name__ == "__main__":
    try:
        # prompt = ""
        # openUrlAndSavePhoto(
        #     getUrlFromPromptAndInputAndMask(
        #         prompt,
        #         "C:\\Users\\Khalid\\Desktop\\khaliddalle\\inputs\\original.png",
        #         "C:\\Users\\Khalid\\Desktop\\khaliddalle\\inputs\\mask.png"
        #     ),
        #     prompt
        # )
        openUrlAndSavePhoto(
            getUrlFromInput(
                "C:\\Users\\Khalid\\Desktop\\khaliddalle\\inputs\\original.png"
            ),
            "iterate living room"
        )
    except Exception as e:
        print(e)
