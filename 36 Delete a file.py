import os
import shutil

file = input("Enter the path of the file to delete: ")

try:
    os.remove(file)
    print("File deleted")
except FileNotFoundError:
    print("The file doesn't exist")
except PermissionError:
    print("You don't have the permission to delete the file")
except IsADirectoryError:
    print("The path is a directory")


# os.rmdir("path") # Remove a empty directory
# shutil.rmtree(path) # Remove directories recursively
