import io

def read(filename):
    location = "D:/Projects/Python/School/Dec/week2/files"
    f = open(f"{location}/{filename}", "r")

    data = f.readlines()
    print(data)

    f.close()

def main():
    read("test.txt")

if __name__ == "__main__":
    main()