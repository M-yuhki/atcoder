n = list(map(int,list(input())))

ans = 0

if(n[0] == 1 and n.count(0) == len(n) -1):
  ans = 10

else:
  for i in range(len(n)):
    ans += n[i]

print(ans)
  
