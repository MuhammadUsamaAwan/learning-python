# while 1==1:
#     print("Help! I'm stuck in a loop!")

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
    if len(name) == 0:
        print("You didn't enter anything!")
    else:
        print("Hello " + name)
