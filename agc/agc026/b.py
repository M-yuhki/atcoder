n = int(input())

for i in range(n):
  a,b,c,d = map(int,input().split())

  flg = False

  t = a % b
  u = b - d
  v = [t]
  while (a >= b and d >= b):
    if(t > c):
      break
    t += u
    if(t > b):
      t = t % b
      if(t in v):
        flg = True
        break
      else:
        v.append(t)

  print(v)
  if(flg):
    print("Yes")
  else:
    print("No")

  #if( (a<b) or (d<b) or ( a > b and a%b > c) or ( d > b and ((a%b)+d)%b > c) or b > h or (a % d > c and b > c) or  (d %b > c and b > c) or (h % b > c and b > c)):
  del(v)

