capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "France": "Paris",
}
print(capitals["India"])
print(capitals.get("Germany"))

capitals.update({"Germany": "Berlin"})
print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())


for key, value in capitals.items():
    print(key, value)
