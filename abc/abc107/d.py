import statistics
n = int(input())
a = list(map(int,input().split()))
p = int(int(n *(n+1)/2)/2 + 1)
ans = a
flg = False
for i in range(2,n):
  for j in range(n-i):
    t = statistics.median_high(a[j:i+j])
    ans.append(t)
    if(ans.count(t) >= p):
      flg = True
      break
  if(flg):
    break
print(statistics.median_high(ans))

