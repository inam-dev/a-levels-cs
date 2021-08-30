i = 0
while i < 4:
    j = 0
    while j < 4:
        if i == j:
            print("1 ", end = '')
        else:
            print("0 ", end = '')

        j += 1

    i += 1

    print()
