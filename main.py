import dalle
import sd2
import sys

from saveutil import openUrlAndSavePhoto


urlFromPromptDict = {
    "dalle": dalle.getUrlFromPrompt,
    "sd2": sd2.getUrlFromPrompt
}

if __name__ == "__main__":
    try:
        prompt = " ".join(sys.argv[1:])
        imageURL = urlFromPromptDict["dalle"](prompt)
        openUrlAndSavePhoto(imageURL, prompt)
    except Exception as e:
        print(e)
