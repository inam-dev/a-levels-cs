a = [0]*4
for i in range(0,4):
    a[i] = [0]*4

for i in range(0,4):
    a[i][i] = 1

for i in range(0,4):
    for j in range(0,4):
        print(f"{a[i][j]} ", end = '')
    print()