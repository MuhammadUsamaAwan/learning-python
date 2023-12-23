try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print("No exceptions encountered!")
finally:
    print("This is the end of the program.")
