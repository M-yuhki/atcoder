x = int(input())

num = list(range(2,32))
print(num)

ans = 1
for i in range(len(num)):
  now = num[i]
  while now < x:
    now = now*num[i]
    if(now <= x and ans <= now):
      ans = now
print(ans)        



