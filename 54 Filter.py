friends = [
    ("Rolf", 16),
    ("Anne", 37),
    ("Charlie", 19),
    ("Bob", 22),
]

age = lambda data: data[1] >= 21

drinking_buddies = list(filter(age, friends))
print(drinking_buddies)
