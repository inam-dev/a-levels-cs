f = 1
while f > 0: 
    sym = input("Input the symbol: ")
    num = int(input("Input the final row number thing (Should be odd): "))
    i = 1

    while (num % 2) == 0:
        num = int(input("Input the final row number thing (Should be odd): "))
    
    rows = int( (num / 2) + 0.5 )

    while rows > 0:
        rows -= 1
        spaces = " " * rows
        
        print(f"{spaces}{sym*i}")

        i += 2