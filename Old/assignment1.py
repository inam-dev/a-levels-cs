a = [0]*4
for i in range(0,4):
    a[i] = [0]*4

j = 3
for i in range(0,4):
    #Array method start
    a[i][j] = 1
    j -= 1
    #Array method End

    # Non-Array method Start
    '''
    while j >= 0:
        if i == j:
            print("1 ", end = '')
        else:
            print("0 ", end = '')
    print()
    '''
    # Non-Array method End

# Array Printing Start
for i in range(0,4):
    for j in range(0,4):
        print(f"{a[i][j]} ", end = '')
    print()
# Array Printing End