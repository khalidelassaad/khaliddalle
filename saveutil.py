import pathlib
import time
import requests
import webbrowser


def openUrlAndSavePhoto(imageURL, prompt):
    try:
        webbrowser.open(imageURL)
        fileSafePrompt = "".join(
            c for c in prompt if (c.isalnum() or c == " "))
        filename = str(int(time.time())) + "_" + \
            "_".join(fileSafePrompt.split(" ")) + ".png"
        filepath = pathlib.Path.cwd() / "outputs" / filename
        response = requests.get(imageURL)
        if response.status_code:
            fp = open(filepath, 'wb')
            fp.write(response.content)
            fp.close()
            print(filepath)

    except Exception as e:
        print(e)
