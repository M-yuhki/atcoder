n = int(input())
target = []
plus = []
for i in range(n):
  x,y = map(int,input().split())
  target.append([x,y])
  z = abs(x)+ abs(y)
  if z not in plus:
    plus.append(z)
oe = list(map(lambda x:x%2,plus))
if(oe.count(0) != 0 and oe.count(1) != 0):
  print(-1)
else:
  d_num = max(plus)
  print(d_num)
  for i in range(d_num-1):
    print("1 ",end="")
  print(1)

  for i in range(n):
    move = ""
    x_move = target[i][0]
    y_move = target[i][1]
    less = d_num - (abs(x_move) + abs(y_move))
    if(x_move >= 0):
      move += "R"*x_move
    else:
      move += "L"*abs(x_move)
    if(y_move >= 0):
      move += "U"*y_move
    else:
      move += "D"*abs(y_move)
    move += "RL"*int(less/2)
    print(move)

