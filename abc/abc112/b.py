n,t = map(int,input().split())
d = 1000000
for i in range(n):
  c,a = map(int,input().split())
  if(c <= d and a <= t):
    d = c
if(d == 1000000):
  print("TLE")
else:
  print(d)

