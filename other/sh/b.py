import math
s = input()
n = int(input())

ans = ""

for i in range(math.ceil(len(s)/n)):
  ans += s[i*n]

print(ans)
