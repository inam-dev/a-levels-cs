'''Display marks greater than or equal to 90 in console from student_marks.txt'''

#   ---┬--- |\   |    /\       /|   /|
#      |    | \  |   /  \     / |  / |
#      |    |  \ |  /----\   /  | /  |
#   ---┴--- |   \| /      \ /   |/   |
#                      11:30 - 12:30 | BDC

import io

def readFile(fileName):
    path = "D:/Projects/Python/School/Dec/week2/files"

    # Opens the file for Reading
    f = open(f"{path}/{fileName}", "r")
    # Saves each line in a text file as a list item
    data = f.readlines()

    for i in range(0, len(data)):
        # Convert `string` values in list to `integer` for comparison
        data[i] = int(data[i])

        # Print the marks (line) if marks are greater than or equal to 90
        if data[i] >= 90:
            print(data[i])

    f.close()

def main():
    readFile("student_marks.txt")

if __name__ == "__main__":
    main()