import os

source = input("Enter the path of the file to move: ")
destination = input("Enter the path of the destination: ")

try:
    if os.path.exists(source):
        print("The file already exists")
    else:
        os.replace(source, destination)
        print("File moved")
except FileNotFoundError:
    print("The file doesn't exist")
