import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def addc(p,b):  
  for i in e[p]:
    if(i == b):
      continue
    c[i] += c[p]
    addc(i,p)

n,q = map(int,input().split())

e = [ [] for i in range(n + 1)]
c = [0]*(n+1)

for i in range(n-1):
  a,b = map(int,input().split())
  e[a].append(b)
  e[b].append(a)

for i in range(q):
  p,x = map(int,input().split())
  c[p] += x

addc(1,-1)

print(*c[1:])
