import requests
from pprint import pprint

from python_translator import Translator

translator = Translator()
result = translator.translate("Hello world!", "russian", "english")

print(result)

def get_red_panda():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animal/red_panda")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
        fact=content['fact']
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    print(content)
get_red_panda()
