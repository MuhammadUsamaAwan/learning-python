import functools

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(functools.reduce(lambda x, y: x + y, letters))
