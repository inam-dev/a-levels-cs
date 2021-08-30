'''Save First 30 even Numbers in a File with their Sum'''

#   ---┬--- |\   |    /\       /|   /|
#      |    | \  |   /  \     / |  / |
#      |    |  \ |  /----\   /  | /  |
#   ---┴--- |   \| /      \ /   |/   |
#                      11:30 - 12:30 | BDC

import io

def fileAppender(path, fileName, data = ""):
    """ Adds text data given in `data` to end of given `fileName` at `path` \n
        Creates a new file if the `fileName` doesn't already exists at `path` """ #<--- Function Description for intelisense 
    f = open(f"{path}/{fileName}", "a")

    if data != "":
        f.write(data)

def outputEvenNums(path, n):
    """ Outputs `n` number of Even numbers and their sum to 'Data.txt' File in `path` folder """ #<--- For intelisense
    i, j, sum = 1, 0, 0
    fileName = "Data.txt"

    while j < n:
        if (i % 2) == 0:
            data = f"{i} \n"
            fileAppender(path, fileName, data)

            sum += i
            j += 1
        i += 1

    fileAppender(path, fileName, f"Sum of above numbers: {sum}")

def main():
    folder = "D:/Projects/Python/School/Dec/week2/files"

    outputEvenNums(folder, 30)

    print("Done")                                                               #<--- Just so the Console is not empty

if __name__ == "__main__":
    main()