def costFinder(unitsUsed):
    if unitsUsed > 500:
        cost = 7
    elif unitsUsed > 300:
        cost = 5
    else:
        cost = 2

    return cost

def totalBillFinder(total, lineRent):
    if total > 2000:
        total *= 1.05

    total += lineRent
    return total

consumed = int(input("Units Consumed: "))
cost = costFinder(consumed)

total = cost * consumed
total = totalBillFinder(total, 150)

print(f"Total Bill:  Rs. {total}")