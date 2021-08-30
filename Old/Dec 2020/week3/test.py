def fun(a, b):
    shorter = min(len(a), len(b))
    count = 0

    for i in range(shorter-1):
        # i in range 3
        #--> i:         In Iterations (for test value)
        #----> 0
        #----> 1
        #----> 2

        a_sub = a[i:i+2]
        #print(a_sub)
        #--> 'te'
        #--> 'es'
        #--> 'st'

        b_sub = b[i:i+2]
        #print(b_sub)
        #--> 'st'
        #--> 'tr'
        #--> 'ti'

        if a_sub == b_sub:
            #print(a_sub == b_sub)
            #--> False
            #--> False
            #--> False

            count = count + 1
    return count
    #count = 0


print( fun("test", "string") )
#--> 0