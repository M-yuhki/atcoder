n = int(input())

before = int(input())
ans = 0
if(before == 0):
  for i in range(n-1):
    now = int(input())
    if(now - before >= 2):
      ans = -1
      break
    elif(now != 0):
      ans += 1
    before = now

else:
  ans = -1

print(ans)
