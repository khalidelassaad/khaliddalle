import os

prompts = [
    "An illustration of a rainbow over a mountain range",
    "A sculpture of a winking octopus",
    "A painting of a red fox in the snow",
    "A drawing of a vibrant bouquet of wildflowers",
    "A photograph of a majestic waterfall",
    "An abstract drawing of a starry night sky",
    "A sculpture of a castle in the clouds",
    "A painting of a monarch butterfly in the garden",
    "A drawing of a sunset over the ocean",
    "An illustration of a magical forest scene"
]


if __name__ == "__main__":
    for prompt in prompts:
        count = 5
        command = prompt + " -n " + str(count)
        interpreter = "/Users/khalidelassaad/Desktop/khaliddalle/.venv/bin/python"
        script = "/Users/khalidelassaad/Desktop/khaliddalle/main.py"

        os.system(interpreter + " " + script + " " + command)
