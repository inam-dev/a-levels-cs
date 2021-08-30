BikeSpace = [[0]*4]*30

Row = 1
while Row <= 30:
    Position = 1
    while Position <= 4:
        BikeReg = input("Bike Reg:")

        if BikeReg != "BK000":
            BikeSpace[Row][Position] = BikeReg
            Position += 1
        else:
            Position = 100
            Row = 100
    Row += 1