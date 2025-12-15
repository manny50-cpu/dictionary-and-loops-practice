# this is what we will use for the video intro to dictionaries
# dictionary = collection of (key:value) pairs
# ordered and changeable. No duplicates

capitals = {"USA": "Washington DC.",
          "India": "New Delhi",
            "China": "bejing", 
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

if capitals.get("Russia"):
    print('That capital exists')
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()
keys = capitals.keys()

for key in capitals.key():
    print(key)

values = capitals.values()
for value in capitals.values():
print(value)
items= capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")