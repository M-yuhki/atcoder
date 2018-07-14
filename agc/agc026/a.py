n = int(input())

slime = list(map(int,input().split()))

b = 0
c = 0 

for i in range(n):
  if(b == slime[i]):
    c += 1
    b = 0
  else:
    b = slime[i]

print(c)
