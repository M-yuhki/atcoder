n,k,q = map(int,input().split())

s = [k-q for i in range(n) ]

for i in range(q):
  t = int(input())
  s[t - 1] += 1


for i in range(n):
  if(s[i] > 0):
    print("Yes")
  else:
    print("No")
