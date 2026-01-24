thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
thisdict['sex'] = 'Male'
print(thisdict)
print(thisdict.get("name"))
print(thisdict["name"])

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
if 'sex' in thisdict:
    print('Sex key is there')

# Change Values
print('Change Values')
thisdict.update({"color": "red"})
print(thisdict)

# Removing Items
print('Removing Items')
print(thisdict)
thisdict.pop('sex')
print(thisdict)
thisdict.popitem()
print(thisdict)
# thisdict.clear()
print(thisdict)


for x in thisdict.keys():
    print(x)
for y in thisdict.values():
    print(y)
for x, y in thisdict.items():
    print(x, y)

thisdictcp = thisdict.copy()
print(thisdictcp)
thisdictdict = dict(thisdict)
print(thisdictdict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x, obj in myfamily.items():
    # print(x, obj)
    for y, z in obj.items():
        print(x, y, z)

keys = ['child1', 'child2', 'child3']
values = [1, 2, 3]
thisdct = dict.fromkeys(keys, values)
print(thisdct)
print(dict(zip(keys, values)))

car = {
"brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x =  car.setdefault('color', 'red')
print(x, car)