import requests, json
data = { 'username' : 'root', 'password' : 'P@$$w0rld' }
headers ={'client-version': '1.23.0','Content-Type': 'application/json'}
r = requests.post('http://192.168.1.16/authenticate', data=json.dumps(data), headers=headers, verify=False)
token = json.loads(r.text)['token']
print(token)
headers = { 'Authorization' : 'Token ' + token  }
print(headers)
rGet = requests.get('http://192.168.1.16/sina/topology/node/' ,headers=headers, verify=False)
print(json.loads(rGet.text))