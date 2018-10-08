import math
n,m =map(int,input().split())
a = int(m/n)
b = m%n
print(math.gcd(a,b))
