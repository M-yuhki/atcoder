import copy
n,m,q = map(int,input().split())
num = [0 for i in range(n)]
for i in range(m):
  l,r = map(int,input().split())
  for j in range(l,r+1):
    num[j-1] += 1

for i in range(q):
  l,r = map(int,input().split())
  d = copy.deepcopy(num)
  e = d[l-1:r]
  hi = e[0]
  mi = e[len(e)-1]
  print(m - (min(e) + max(hi,mi)))
