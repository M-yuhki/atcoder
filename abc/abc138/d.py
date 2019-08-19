def adx(p,oya,tox,total):
  tox[p] += total
  total = tox[p]
  if(len(oya[p]) == 0):
    return 0

  else:
    for i in oya[p]:
      adx(i,oya,tox,total)

  return 0

n,q = map(int,input().split())

oya = [ [] for i in range(n + 1)]
tox = [0 for i in range(n + 1)]

for i in range(n-1):
  a,b = map(int,input().split())
  oya[a].append(b)

for i in range(q):
  p,x = map(int,input().split())
  tox[p] += x

_ = adx(1,oya,tox,0)

tox.pop(0)

print(*tox)
