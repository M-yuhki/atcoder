n,x = map(int,input().split())
a = list(map(int,input().split()))
a.append(x)
a.sort()
d = [1000000000]
e = []
flg = False
for i in range(len(a)-1):
  t = a[1+i] - a[i]
  e.append(t)
  if(t < d[0]):
    d.insert(0,t)
  if(t == 1):
    flg = True
    break
if(flg):
  print(1)
else:
  d.sort()
  l = len(d)
  ans = 1
  for i in range(l):
    u = list(map(lambda x: x% d[l - 1 - i],e))
    if(u.count(0) == n):
      ans = d[l-1-i]
      break
  if(ans == 1):
    k = d[0]
    f = []
    j = 2
    while True:
      s = int(k/j)
      if(k % j == 0):
        f.insert(0,s)
      if(s < 1):
        break
      j += 1
    q = len(f)
    for i in range(q):
      u = list(map(lambda x: x% f[q - 1 - i],e))
      if(u.count(0) == n):
        ans = f[q-1-i]
        break

  print(ans)
