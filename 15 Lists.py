food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food[0])
food[0] = "sushi"
print(food[0])

for x in food:
    print(x)

food.append("ice cream")
print(food)

food.remove("hotdog")
print(food)

food.pop()
print(food)

food.insert(0, "cake")
print(food)

food.sort()
print(food)

food.reverse()
print(food)

food.clear()
print(food)
