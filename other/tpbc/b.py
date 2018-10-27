a,b,k = map(int,input().split())

for i in range(k):
  if(i%2 == 0):
    if(a%2==1):
      a -= 1
    s = int(a/2)
    a -= s
    b += s
  else:
    if(b%2==1):
      b -= 1
    s = int(b/2)
    b -= s
    a += s

print("{} {}".format(a,b))
