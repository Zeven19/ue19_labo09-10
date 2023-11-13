import requests

url = "https://rickandmortyapi.com/api/character/"

reponse = requests.get(url)

if reponse.status_code == 200:
    donnee = reponse.json()
    print(donnee)
else:
    print("Erreur")
