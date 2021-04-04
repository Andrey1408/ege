a = open("24-5.txt")
text = a.read()
mx = 0
d = 1
for i in range(1,len(text)):
    if text[i] == text[i-1] and text[i] == ')':
        d += 1
        if d > mx:
            mx = d
    else:
        d = 1
print(mx)





















