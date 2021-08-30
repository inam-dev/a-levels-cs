even = 0
odd = 0

min = 10000
max = 0

a = [0]*4
for i in range(1,4):
    a[i] = [0]*3

    # For User Input
    for j in range(1,3):
        a[i][j] = int(input(f"Number {i}-{j}: "))
 
for i in range(1,4):
    for j in range(1,3):
        if a[i][j] > max:
            max = a[i][j]

        if a[i][j] < min:
            min = a[i][j]

        if (a[i][j] % 2) == 0:
            even += 1
        else:
            odd += 1

print(f"Even: {even}")
print(f"Odd: {odd}")
print()
print(f"Min: {min}")
print(f"Max: {max}")