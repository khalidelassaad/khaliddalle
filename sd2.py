import os
import webbrowser
import replicate
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("REPLICATE_API_TOKEN")

model = replicate.models.get("stability-ai/stable-diffusion")
url = model.predict(prompt="a 19th century portrait of a wombat gentleman")[0]
webbrowser.open(url)
