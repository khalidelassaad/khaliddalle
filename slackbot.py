import json
import dalle

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

with open("secrets.json", "r") as secretsFile:
    secretsJson = json.loads(secretsFile.read())

slackData = secretsJson["slack"]

app = App(
    token=slackData["bot_oauth_token"],
)


def getPromptAndImageURLFromMessageBody(body):
    # Guard on user is me
    if not body.get("event").get("user") == slackData["me"]:
        return

    # Guard on channel exists
    channel = body.get("event").get("channel")
    if not channel:
        return

    # Guard on command is !dalle
    text = body.get("event").get("text")
    if not text:
        return
    if not text.split(" ")[0] == "!dalle":
        return

    # Extract prompt and get image url

    prompt = " ".join(text.split(" ")[1:])

    imageUrl = dalle.getUrlListFromPrompt(prompt)

    return (prompt, imageUrl, channel)


@app.event("message")
def handle_message_events(body, say):
    print(body.get("event").get("user"))
    print(body.get("event").get("text"))

    result = getPromptAndImageURLFromMessageBody(body)
    if not result:
        return

    prompt, imageUrl, channel = result

    headerText = prompt
    blocks = [
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": prompt,
            },
            "image_url": imageUrl,
            "alt_text": prompt
        },

    ]
    say(text=headerText, blocks=blocks, channel=channel)


if __name__ == "__main__":
    SocketModeHandler(app, slackData["app_token"]).start()
