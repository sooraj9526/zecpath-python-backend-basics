# File Reader Practice


try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except FileNotFoundError:
    print("The file was not found.")