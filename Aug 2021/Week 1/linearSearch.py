data = [11, 22, 31, 15, 100]
i = -1
search = input("Enter Number to search for: ")
found = False

# for j in range(0, len(data)):
#     if int(search) == data[i]:
#         found = True
#         i = j

while (i < len(data)-1) and not found:
    i += 1
    if int(search) == data[i]:
        found = True

if found:
    print(f"Found at index: {i}")
else:
    print("Not Found")