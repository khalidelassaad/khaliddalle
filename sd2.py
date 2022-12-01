import replicate
from dotenv import load_dotenv

load_dotenv()

def getUrlFromPrompt(prompt):
    model = replicate.models.get("stability-ai/stable-diffusion")
    url = model.predict(prompt=prompt)[0]
    return url
