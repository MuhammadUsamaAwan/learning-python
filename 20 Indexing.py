name = "john Doe"
if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:4].upper()
print(first_name)

last_name = name[5:].lower()
print(last_name)

last_character = name[-1]
print(last_character)
