def count(p):
  count_r = 0
  for i in range(len(p)):
    if(i == p[i]):
      count_r += 1
  return count_r

def swap(p,x,y):
  i = p[x]
  p[x] = p[y]
  p[y] = i


def bar(p,table):
  for i in range(len(table)):
    x = table[i][0]-1
    y = table[i][1]-1
    if(x == p[y] and y == p[x]):
      swap(p,x,y)
    elif(x == p[y] or y == p[x]):
      swap(p,x,y)
      bar(p,table)

s = input().rstrip().split()
n = int(s[0])
m = int(s[1])

t = input().rstrip().split()
p = list(map(lambda x:int(x),t))

table = []

for i in range(m):
  u = input().rstrip().split()
  table.append([int(u[0]),int(u[1])])

bar(p,table)
print(count(p))
