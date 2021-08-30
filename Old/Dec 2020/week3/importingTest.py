import fileSearch as fs

def main():
    path = "D:/Projects/Python/School/Dec/week3/files"

    result = fs.searchFile(path, "std.txt", input("Search for: "))
    print(result)

if __name__ == "__main__":
    main()