f = open("27-3b.txt")
d = []
s = 0
mr1 = 10000
mr2 = 10000
mr3 = 10000
mr4 = 10000
for i in f:
    a,b = map(int,i.split())
    s += min(a,b)
    if abs(a-b) % 3 == 1 and abs(a-b) < mr1:
        mr1 = abs(a-b)
    elif abs(a-b) % 3 == 1 and abs(a-b) < mr2:
        mr2 = abs(a-b)
    elif abs(a-b) % 3 == 2 and abs(a-b) < mr3:
        mr3 = abs(a-b)
    elif abs(a-b) % 3 == 2 and abs(a-b) < mr4:
        mr4 = abs(a-b)

if s % 3 == 0:
    print(s)
elif s % 3 == 1:
    if (s + mr3) < (s + mr1 + mr2):
        print(s + mr3)
    else:
        print(s + mr1 + mr2)

elif s % 3 == 2:
    if (s + mr1) < (s + mr3 + mr4):
        print(s + mr1)
else:
    print(s + mr3 + mr4)







