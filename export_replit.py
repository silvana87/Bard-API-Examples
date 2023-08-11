import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)
#response = bard.get_answer("Qué es el procesamiento de lenguaje Natural")['content']
#print(response)


bard_answer = bard.get_answer("Give me python code to connect to database")
url = bard.export_replit(bard_answer['code'], bard_answer['program_lang'])
print(url['url'])
