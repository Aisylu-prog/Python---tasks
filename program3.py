s = [int(i)for i in input().split()]
n = len(s)
t = ''
tr = ''
for i in range(0, n):
    if i<(n-1) and n!=1:
        h = str(s[i-1]+s[i+1])+' '
    if i==(n-1) and n!=1:
        h = str(s[i-1]+s[0])+' '
    if n==1:
        h = s[0]
    t = (t + str(h))
print(t)