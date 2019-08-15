n = int(input())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[i] + a[i])

ans = s[n] + 1
for y in range(2,n-1):
　# 切れ込みはa[y]とa[y+1]の間
  p = s[y]

  xa = -1
  xdiff = s[n] + 1
  za = -1
  zdiff = s[n] + 1
  for x in range(y+1):
    xtdiff = p - s[x]*2
    if(xtdiff <= xdiff):
      xa = x


  for z in range(y+2,n+1):
    ztdiff = s[n] - s[z]*2 + p 
    if(ztdiff <= zdiff):
      za = z






print(ans)
