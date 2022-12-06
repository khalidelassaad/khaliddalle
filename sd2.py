import replicate
from dotenv import load_dotenv

load_dotenv()


def getUrlFromPrompt(prompt):  # TODO: Receive and use "count" arg
    model = replicate.models.get("stability-ai/stable-diffusion")
    url = model.predict(prompt=prompt)[0]
    return url
