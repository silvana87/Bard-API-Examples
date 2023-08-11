import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)
audio = bard.speech("hello world, my name is Silvana!")
with open("bard.ogg", "wb") as f:
    f.write(bytes(audio['audio']))
