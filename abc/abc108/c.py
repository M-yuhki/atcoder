import math

n, k = map(int, input().split())

ans = int(math.pow(int(n/k),3))

if(k % 2 == 0):
  m = int( (n+int(k/2))/ k )
  ans += int(math.pow(m,3))

print(ans)
