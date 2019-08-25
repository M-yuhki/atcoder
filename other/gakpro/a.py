m,d = map(int,input().split())

ans = 0;

if(d >= 22):
  for i in range(1,m+1):
    for j in range(20,d+1):
      d1 = j%10
      d10 = int(j/10)
      if(d1 >= 2 and d10 >= 2 and i == d1*d10):
        ans += 1

print(ans)
