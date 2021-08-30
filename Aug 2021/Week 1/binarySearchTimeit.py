data = [78, 92, 117, 128, 312, 698, 825, 906, 1007, 1095, 1132, 1332, 1415, 1430, 1962, 2017, 2180, 2193, 2229, 2366, 2448, 2548, 2573, 2584, 2609, 2658, 2740, 2844, 2925, 2949, 2950, 3046, 3226, 3402, 3583, 3724, 3951, 3962, 4141, 4203, 4214, 4217, 4270, 4277, 4328, 4369, 4418, 4480, 4592, 4649, 4653, 5099, 5217, 5269, 5646, 5748, 5868, 5881, 5990, 6507, 6722, 6802, 6878, 6942, 7049, 7091, 7177, 7224, 7296, 7412, 7584, 7632, 7684, 7755, 8087, 8121, 8195, 8202, 8216, 8222, 8290, 8423, 8519, 8659, 8740, 8759, 9089, 9184, 9216, 9266, 9280, 9288, 9472, 9485, 9543, 9729, 9796, 9931, 9982]
def search(data):
    search = 4649
    found = False
    x, y = 0, len(data)

    i = 0
    while not found:
        m = int( (x + y) / 2 )
        #print(m)

        if data[m] == search:
            found = True
        else:
            i += 1
            if i > len(data):
                #print("exit \n exit \n exit \n exit")
                exit()

            if data[m] > search:
                y = m - 1
            else:
                x = m + 1

    if found:
        #print(f"Found at index: {m}")
        pass
    else:
        #print("Not Found")
        pass

import timeit

print(timeit.timeit(f'search({data})', globals=globals(), number=1000000))