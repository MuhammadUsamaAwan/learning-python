temp = input("What is the temperature outside?: ")
temp = int(temp)
if temp >= 0 and temp <= 30:
    print("The temperature is good today")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
    print("Stay inside")

if not (temp >= 0 and temp <= 30):
    print("The temperature is bad today")
    print("Stay inside")
elif not (temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside")
