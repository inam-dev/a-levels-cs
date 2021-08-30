data = [5, 7, 9, 20, 60, 80]

def binarySearch(searchItem):
    found = False
    lowIndex, highIndex = 0, len(data)

    while (highIndex >= lowIndex) and not found:
        midIndex = int((lowIndex + highIndex) / 2)
        if searchItem == data[midIndex]:
            index = midIndex
            found = True
        else:
            if searchItem == data[midIndex]:
                highIndex = midIndex - 1
            else:
                lowindex = midIndex + 1
    
    if found:
        print(f"{searchItem} found at {index}")
    else:
        print(f"{searchItem} Not Found")


binarySearch(80)