n = int(input())
s = input().rstrip().split()
t = list(map(lambda x:int(x),s))
t.sort(reverse=True)  
a = 0
b = 0
for i in range(n):
  if(i%2==0):
    a += t[i]
  else:
    b += t[i]

print(a-b)
