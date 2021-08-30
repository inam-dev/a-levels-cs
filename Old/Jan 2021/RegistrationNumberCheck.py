def ValidateRegistration(Registration): # Registration is String
    p1, p2, p3 = 0, 0, 0        # Integer
    regLen = len(Registration)  # Integer
    c = ""           # String
    result = False   # Boolean

    if regLen < 6 or regLen > 9:
        return False

    for i in range(1, regLen+1):
        c = Registration[i-1]

        if i <= 3:
            if c >= "A" and c <= "Z":
                p1 += 1

        if i >= 4 and i <= 5:
            if int(c) >= 0 and int(c) <= 9:
                p2 += 1

        if i >= 6:
            if c >= "A" and c <= "Z":
                p3 += 1
    
    if p1 == 3 and p2 == 2 and p3 == (regLen - 5):
        result = True

    return result


print(  ValidateRegistration("AaA00AAAAB")  )
print(  ValidateRegistration("AAA00")       )
print(  ValidateRegistration("AdA00AWAA")   )
print()
print(  ValidateRegistration("ADA55AWLK")   )
print(  ValidateRegistration("ARL98DFX")    )
print(  ValidateRegistration("AAM63JA")     )
print(  ValidateRegistration("AFY40N")      )