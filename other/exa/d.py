import math

P = 1000000007

n,x = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
a = []

m = s.pop(0)

k = n - 1

ans = (x%m) * math.factorial(k)%P

k -= 1

while k >= 0:
  print("***")
  print(a)
  print(s)
  print(k)
  t = x
  u = math.factorial(k)
  print(u)
  v = 0
  for i in a:
    t = t % i
  for j in s:
    v += ((t % j)%m) * u
  ans += v % P
  if(len(s) == 0):
    break
  else:
    a.append(s.pop(len(s)-1))

  k -= 1


print(ans)
