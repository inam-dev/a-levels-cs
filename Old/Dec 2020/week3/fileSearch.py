import io

def createTxt(path, filename, data):
    f = open(f"{path}/{filename}","w")

    f.write(data)
    f.close()

def searchFile(path, fileName, search):
    found = False
    location = 0

    f = open(f"{path}/{fileName}", "r")
    data = f.readlines()

    for i in range(0, len(data)):
        line = data[i][:-1]

        if line == search:
            found = True
            location = i + 1

    if found:
        return f"Found at line number {location}"
    else:
        return "Not found"


def main():
    path = "D:/Projects/Python/School/Dec/week3/files"
    search = input("Search for: ")

    fileFound = searchFile(path, "std.txt", search)
    print(fileFound)


if __name__ == "__main__":
    main()