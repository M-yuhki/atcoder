import math

s = input().rstrip().split()

a = int(s[0])
b = int(s[1])
c = int(s[2])

k = int(input())

m = max(a,b,c)

n = math.pow(2,k)

ans = a + b + c + m*(n-1)

print("{}".format(int(ans)))
