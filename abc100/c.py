n = int(input())


s = list(map(int,list(input().rstrip().split())))

count = 0

for i in range(n):
  target = s[i]
  while s[i] % 2 == 0:
    if(target % 2 == 1):
      break
    else:
      count += 1
      target = int(target/2)

print(count)
