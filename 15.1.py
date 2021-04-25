m = 0
for a in range(1,1001):
    t = 0
    for x in range(1,10001):
        if ((a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))) == False:
            t = 1
            break
    if t == 0 and a > m:
        m = a
print(m)