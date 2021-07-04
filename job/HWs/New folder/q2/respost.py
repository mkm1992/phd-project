import requests, json
rGet = requests.post('http://localhost:8080/Mashhad', verify=False)
print(rGet.text)