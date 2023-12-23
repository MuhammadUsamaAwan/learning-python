cities_in_f = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
cities_in_c = {key: round((value - 32) * 5 / 9) for (key, value) in cities_in_f.items()}
print(cities_in_c)

desc_cities_in_f = {
    key: ("warm" if value >= 70 else "cold") for (key, value) in cities_in_f.items()
}
print(desc_cities_in_f)
