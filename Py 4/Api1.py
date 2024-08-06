#Fist py API

import requests

URL = "https://frasedeldia.azurewebsites.net/api/phrase"

respuesta = requests.get(URL)
data = respuesta.json()
print(data["phrase"])
