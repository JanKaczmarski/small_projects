import requests
import json
import webbrowser
from pprint import pprint
from enum import IntEnum

choice = int(input("Wybierz 5 faktów o kocie:1, lub psie:2"))



params = {
    "amount" : 5,
    "animal_type" : "dog"
    }

r = requests.get('https://catfact.ninja/facts/random', params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    if(choice == 1):
        for cat in content:
            print(cat["text"])
    elif(choice == 2):
        for cat in content:
            print(cat["text"])
        

