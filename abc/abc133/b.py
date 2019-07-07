import math

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

n,d=map(int,input().split())

x=[]
for i in range(n):
  x.append(list(map(int,input().split())))


ans = 0
for i in range(n):
  for j in range(n-i-1):
    a = i
    b = i+j+1
    t = 0
    for k in range(d):
      t += math.pow(abs(x[a][k] - x[b][k]),2)

    t = math.sqrt(t)
    if(is_integer_num(t)):
      ans += 1

print(ans)
