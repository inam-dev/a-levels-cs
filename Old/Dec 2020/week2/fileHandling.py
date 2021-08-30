import io

filesFolder = "D:/Projects/Python/School/Dec/week2/files"
f = open(f"{filesFolder}/test.txt", "w")

for i in range (1, 6):
    f.write(f"{i}: Hello Worldaaaaaaa \n")

f.close()