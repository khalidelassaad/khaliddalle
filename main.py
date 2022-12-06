import dalle
import sd2
import sys
import argparse

from saveutil import openUrlAndSavePhoto

CURRENT_MODEL = "dalle"

parser = argparse.ArgumentParser(
    prog='Dalle',
    description='Send a prompt to DallE or other AI Art API',
    epilog='Current Model: ' + CURRENT_MODEL)
parser.add_argument('prompt', nargs="+")
parser.add_argument('-n', '--number', default=1)
args = parser.parse_args()


urlFromPromptDict = {
    "dalle": dalle.getUrlListFromPrompt,
    "sd2": sd2.getUrlFromPrompt  # TODO: add optional index and handle count
}

if __name__ == "__main__":
    prompt = " ".join(args.prompt)
    count = int(args.number)
    imageURLs = urlFromPromptDict[CURRENT_MODEL](prompt, count)
    for index, imageURL in enumerate(imageURLs):
        openUrlAndSavePhoto(imageURL, prompt, index)
