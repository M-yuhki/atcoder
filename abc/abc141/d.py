import bisect

n,m = map(int,input().split())

a = list(map(int,input().split()))

p = 0
q = -1
list.sort(a,reverse= True)


for i in range(m):
  x = int(a[p]/2)
  a[p] = x
  if(q == -1):
    q = x

  if(p == n -1):
    q = -1
    p = 0
    list.sort(a,reverse=True)
  elif(a[p+1] < q):
    q = -1
    p = 0 
    list.sort(a,reverse=True)
  else:
    p += 1 
 

print(sum(a))
