import pathlib
import time
import requests
import webbrowser
from inspect import getsourcefile


def openUrlAndSavePhoto(imageURL, prompt, index):
    webbrowser.open(imageURL)
    fileSafePrompt = "".join(
        c for c in prompt if (c.isalnum() or c == " "))
    filename = str(int(time.time())) + "_" + \
        str(index) + "_" + \
        "_".join(fileSafePrompt.split(" ")) + ".png"
    filepath = ((pathlib.Path(getsourcefile(lambda: 0)).parent /
                "outputs") / filename).resolve()
    response = requests.get(imageURL)
    if response.status_code:
        fp = open(filepath, 'wb')
        fp.write(response.content)
        fp.close()
        print(filepath)


if __name__ == "__main__":
    print(((pathlib.Path(getsourcefile(lambda: 0)).parent /
          "outputs") / "image.png").resolve())
