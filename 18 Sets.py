# Description: Sets are unordered collections of unique elements.

utensils = {"fork", "spoon", "knife"}
print(utensils)

utensils.add("napkin")
print(utensils)
utensils.remove("fork")
print(utensils)
# utensils.clear()
# print(utensils)

dishes = {"bowl", "plate", "cup"}
print(dishes)
utensils.update(dishes)
print(utensils)

dinner_table = utensils.union(dishes)
print(dinner_table)

print(dinner_table.difference(dishes))
