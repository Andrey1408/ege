for a in range(1,500):
    t = 0
    for x in range(1,1000):
        if ((x & 41 != 0) <= ((x & 33 == 0) <= (x & a != 0))) == False:
            t = 1
            break
    if t == 0:
        print(a)