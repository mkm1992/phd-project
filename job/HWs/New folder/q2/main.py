import json
f = open('city.json',)
data = json.load(f)
print(data)
city = input("city\n")
print(data[city])
dict_sample = dict({city:data[city]})
print(json.dumps(dict_sample))
