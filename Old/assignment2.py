array = ["."]*37

for i in range(1,37):
    print(f"{array[i]} ", end = '')
    if i % 6 == 0 and i > 1:
        print()

    if i == 12:
        array[i+1] = "A"
    if i == 24:
        array[i+1] = "B"
    if i == 35:
        array[i+1] = "Y"