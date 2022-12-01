import pathlib
import webbrowser
import dalle
import sd2
import time
import requests
import sys

getUrlFromPrompt = dalle.getUrlFromPrompt
# getUrlFromPrompt = sd2.getUrlFromPrompt

def openUrlAndSavePhoto(imageURL):
    try:
        webbrowser.open(imageURL)

        filename = str(int(time.time())) + "_" + "_".join(prompt.split(" ")) + ".png"
        filepath = pathlib.Path.cwd() / "outputs" / filename
        response = requests.get(imageURL)
        if response.status_code:
            fp = open(filepath, 'wb')
            fp.write(response.content)
            fp.close()
            print(filepath)
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
        prompt = " ".join(sys.argv[1:])
        imageURL = getUrlFromPrompt(prompt)
        openUrlAndSavePhoto(imageURL)