import json


x = '{"name":"naga", "age":29}'
y = json.loads(x)
print(y, type(y), len(y))
print(y['age'])

a = {'name': 'naga', 'age': 29}
b = json.dumps(a)
print(b, type(b), len(b))

print(json.dumps(['naga', 'raju']), type(json.dumps(['naga', 'raju'])))
print(json.dumps(('naga', 'raju')), type(json.dumps(('naga', 'raju'))))
print(json.dumps('naga'), type(json.dumps('naga')))
print(json.dumps(1), type(json.dumps(1)))
print(json.dumps(1.0), type(json.dumps(1.0)))
print(json.dumps(True), type(json.dumps(True)))
print(json.dumps(False), type(json.dumps(False)))
print(json.dumps(None), type(json.dumps(None)))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=2))
print(json.dumps(x, indent=2, sort_keys=True))
print(json.dumps(x, indent=2, sort_keys=True, separators=('_', '->')))

with  open('sample_JSON.json', 'r') as file:
    data = json.load(file)
    print(data, type(data))
    json.dump(data, open('sample_JSON_wrote.json', 'w'), indent=2)

