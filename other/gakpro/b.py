import sys
sys.setrecursionlimit(10**9)

n,k = map(int,input().split())

a = list(map(int,input().split()))

MOD = pow(10,9) + 7

p = 0

c = 0
d = 0
e = 0
for i in range(n):
  for j in range(i+1,n):
    e += 1
    """
    if(a[i] > a[j]):
      c += 1
      d += 1
    elif(a[i] < a[j]):
      d += 1
    """
print(e)

ans = int(c * k % MOD) + int( (k *(k-1)/2) % MOD * d)
ans = int(ans%MOD)

print(ans)


