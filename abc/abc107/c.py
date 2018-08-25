n,k = map(int,input().split())
row = list(map(int,input().split()))

p = 10000000000000000
i = 0
j = 1
while i + k <= n:
  if(row[i]*row[i+k-1] < 0):
    l = abs(row[i])
    r = abs(row[i+k-1])
    ma = max(l,r)
    mi = min(l,r)
    t = mi*2 + ma
    
    if(t < p):
      p = t
  elif(row[i] < 0):
    t = abs(row[i])
    if(t < p):
      p = t
  else:
    t = row[i+k-1]
    if(t < p):
      p = t
  i += 1

print(p)
