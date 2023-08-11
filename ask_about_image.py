import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)

image = open('prueba.jpg', 'rb').read() # (jpeg, png, webp) are supported.
bard_answer = bard.ask_about_image('What is in the image?', image)
print(bard_answer)