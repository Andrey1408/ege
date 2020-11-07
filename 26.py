a = open('28138.txt')
user = []
users = []
sum1 = 0
maxi = 0
t = 0
n = 1929
s = 6589
for line in a:
    user.append(str(line))
length = user.pop(0)
for line in user:
    users.append(int(line))
users.sort()
for i in range(n):
    if sum1 + users[i] <= s:
        sum1 = sum1 + users[i]
        maxi = i
t = users[maxi]
for i in range(maxi,n):
    if (sum1-t) + users[i] <= s:
        sum1 = sum1 - t + users[i]
        t = users[i]
print(maxi,t)





