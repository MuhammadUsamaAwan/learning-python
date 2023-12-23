def hello(**kwargs):
    print("Hello", end=" ")
    for value in kwargs.values():
        print(value, end=" ")


hello(first="John", middle="Smith", last="Doe")
