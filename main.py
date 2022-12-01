import pathlib
import webbrowser
import dalle
import sd2
import time
import requests
import sys

getUrlFromPrompt = dalle.getImageUrl
getUrlFromPrompt = sd2.getImageUrl

if __name__ == "__main__":
    try:
        prompt = " ".join(sys.argv[1:])
        imageURL = getUrlFromPrompt(prompt)
        webbrowser.open(imageURL)

        filename = str(int(time.time())) + "_" + prompt + ".png"
        filepath = pathlib.Path.cwd() / "outputs" / filename
        response = requests.get(imageURL)
        if response.status_code:
            fp = open(filepath, 'wb')
            fp.write(response.content)
            fp.close()
            print(filepath)
    except Exception as e:
        print(e)