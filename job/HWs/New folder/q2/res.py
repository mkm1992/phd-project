import requests, json
rGet = requests.get('http://localhost:8080/Mashhad', verify=False)
print(rGet.text)