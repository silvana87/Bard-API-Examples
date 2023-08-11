import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)
response = bard.get_answer("Qué es el procesamiento de lenguaje Natural")['content']
print(response)
