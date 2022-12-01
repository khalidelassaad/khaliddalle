import dalle
import sys

from saveutil import openUrlAndSavePhoto


getUrlFromPrompt = dalle.getUrlFromPrompt
# getUrlFromPrompt = sd2.getUrlFromPrompt

if __name__ == "__main__":
    try:
        prompt = " ".join(sys.argv[1:])
        imageURL = getUrlFromPrompt(prompt)
        openUrlAndSavePhoto(imageURL, prompt)
    except Exception as e:
        print(e)