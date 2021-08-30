"""
Enter Number to search
Find Number
Number found in array
"""
# import random

found = False
location = ""
count = 0

a = [[0]*3]*3
# for i in range(0,3):
#     a[i] = [0]*3

# for i in range(0,3):
#     for j in range(0,3):
#         a[i][j] = random.randint(0,1000)

# TEST DATA
a[0][0] = 10
a[0][1] = 52
a[0][2] = 66

a[1][0] = 57
a[1][1] = 85
a[1][2] = 66

a[2][0] = 87
a[2][1] = 96
a[2][2] = 66
# TEST DATA END


search = int(input("Enter the number to search for: "))

for i in range(0,3):
    for j in range(0,3):
        if count == 0:
            if a[i][j] == search:
                found = True
                location += f"[{i}][{j}]"
                count += 1
        else:
            if a[i][j] == search:
                location += f" And [{i}][{j}]"
                count += 1

if count > 1:
    theS = "s "
else:
    theS = " "

print()

if found:
    print(f"Number found at location{theS}{location}")
else:
    print("Number not found in this array")