n = int(input())

a = list(map(int,input().split()))
list.sort(a,reverse=True)
x = a.pop(0)
y = a.pop(0)

for i in a:
  xt = x^i
  yt = y^i
  if(xt + y >= yt + x):
    x = xt
  else:
    y = yt

print(x + y)
