n = int(input())

b = 0
p = [0,0]

flg = True



for i in range(n):
  t,x,y = map(int,input().split())

  diff = abs(x - p[0]) + abs(y - p[1])
  time = t - b
  if(diff > time or time%2 != diff %2):
    flg = False
    break
  else:
    b = t
    p[0] = x
    p[1] = y

if flg:
  print("Yes")
else:
  print("No")



