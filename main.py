import json
import re

from datetime import date
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

with open("secrets.json", "r") as secretsFile:
    secretsJson = json.loads(secretsFile.read())

slackData = secretsJson["slack"]

app = App(
    token=slackData["bot_oauth_token"],
)

subjectAndSrcAToDestChannelMappings = {
    ("Algolia CLI Metrics", "C042357Q7NF"): "C0417DU5MPH"
}


def matchMessageToMappingGuard(body):
    # Guard on has event
    if not (body.get("event")):
        return

    # Guard on has files
    if not (body.get("event").get("files") and
            len(body.get("event").get("files")) > 0):
        return

    # Guard on username is "Email"
    if not body.get("event").get("files")[0].get("username") == "Email":
        return

    # Guard on Sender = no-reply@tableau.com
    if not (body.get("event").get("files")[0].get("from") and
            len(body.get("event").get("files")[0].get("from")) > 0 and
            body.get("event").get("files")[0].get("from")[0].get("address") == "no-reply@tableau.com"):
        return

    # Guard on Subject exists
    if not (body.get("event").get("files")[0].get("subject")):
        return

    # Guard on Channel exists
    if not (body.get("event").get("channel")):
        return

    # Extract subject, imageUrl, sourceChannel, destinationChannel
    subject = body.get("event").get("files")[0].get("subject")
    imageUrl = re.search(r"<img src=\"(.*?)\">", str(body)).group(1)
    sourceChannel = body.get("event").get("channel")

    # Guard on no (subject, sourceChannel) -> destinationChannel mapping
    destinationChannel = subjectAndSrcAToDestChannelMappings.get(
        (subject, sourceChannel))
    if not destinationChannel:
        return

    return (subject, imageUrl, destinationChannel)


@ app.event("message")
def handle_message_events(body, say):
    match = matchMessageToMappingGuard(body)

    title, imageUrl, destinationChannel = match
    headerText = title + " - " + str(date.today())
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": headerText
            }
        },
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": title,
            },
            "image_url": imageUrl,
            "alt_text": title
        },

    ]
    say(text=headerText, blocks=blocks, channel=destinationChannel)


if __name__ == "__main__":
    SocketModeHandler(app, slackData["app_token"]).start()
