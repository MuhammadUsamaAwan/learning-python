def read_file(path):
    try:
        with open(path) as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")


path = input("Enter the path of the file: ")
read_file(path)
