n,m = map(int,input().split())
bridge = [n+1 for i in range(n)]
for i in range(m):
  a,b = map(int,input().split())
  if(bridge[a-1] > b - 1):
    bridge[a-1] = b - 1

count = 0
p = 0
print(bridge)
while True:
  if(bridge[p:].count(n+1) == len(bridge[p:])):
    q = p
    while bridge[q:].count(n+1) == len(bridge[q:]):
      if(bridge[q-1] <= p):
        break
      elif(bridge[q-1] > p and bridge[q-1] != n+1):
        count += 1
        break
    break
  else:
    p = bridge[p]
    count += 1
print(count) 
