import os


def file_detection(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            print("It is a file")
        elif os.path.isdir(path):
            print("It is a directory")
    else:
        print("File not found")


path = input("Enter the path of the file: ")
file_detection(path)
