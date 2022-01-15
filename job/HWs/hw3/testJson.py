import json
  
# Opening JSON file
with open('city.json') as json_file:
    data = json.load(json_file)
print(data)