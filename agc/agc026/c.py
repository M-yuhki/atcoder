def check(x,y):
  if(x == y):
    return False
  else:
    return True

n = int(input()) 
t = input()
s = []
for i in range(n):
  s.append(t[i*2])
  s.append(t[i*2+1])

a = list(filter(check("c"),s))

print(a)
