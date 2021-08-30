def totalerFunc(t):
    return t * 1.05

def fazoolFunc1():
    return 2

def fazoolFunc2():
    return 5

def fazoolFunc3():
    return 7

def fazoolInputFunc(text):
    return int(input(text))

def fazoolReturner(r):
    return r

def fazoolMultiplier(a, b):
    return a * b

def fazoolPrinter(total):
    print(f"Total Bill: Rs. {total}")

cost = fazoolFunc3()
def FazoolLineRent():
    return 150
total = 0

consumed = fazoolInputFunc("Units Consumed: ")


if consumed <= fazoolReturner(300):
    cost = fazoolFunc1()
elif consumed <= fazoolReturner(500):
    cost = fazoolFunc2()
else:
    cost = fazoolFunc3()

total = fazoolMultiplier(cost, consumed)

if total > fazoolReturner(2000):
    total = totalerFunc(total)

total += FazoolLineRent()

fazoolPrinter(total)