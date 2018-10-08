n = int(input())
x = []
y = []
h = []
for i in range(n):
   a,b,c = map(int,input().split())
   x.append(a)
   y.append(b)
   h.append(c)
   
ans = [-1,-1,-1]
h_c = 0

p = -1

for i in range(len(h)):
  if(h.count(h[i]) >= 3):
    p = h[i]
    break


if(p != -1):
  filed=[[0,0,0],[0,0,0],[0,0,0]]
  for i in range(3):
    t = c.index(p)
    field[i][0] = x[t]
    field[i][1] = y[t]

  if(field[0][0] == filed[1][0]):
    ans = [field[0][0],field[2][1],p + int(abs(filed[0][1] - field[1][1])/2)]
  elif(field[0][0] == filed[2][0]):
    ans = [field[0][0],field[1][1],p + int(abs(filed[0][1] - field[2][1])/2)]
  else:
    ans = [field[1][0],field[0][1],p + int(abs(filed[1][1] - field[2][1])/2)]







