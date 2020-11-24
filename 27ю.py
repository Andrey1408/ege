a = []
m = 17
maxi = 0
maxj = 0
s = 0
b = open('27991_B.txt')
for line in b:
    a.append(int(line))
length = a.pop(0)
for i in range(0,length):
    for j in range(i+1,length):
        if ((a[i]-a[j])>0 or (a[j]-a[i])>0 and (a[i]-a[j])%2==0 or (a[j]-a[i])%2==0) and (a[i]%17==0 or a[j]%17==0):
            if a[i] + a[j] > maxi + maxj:
                maxi = a[i]
                maxj = a[j]
print(maxi,'',maxj)
