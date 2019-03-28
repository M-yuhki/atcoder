def chmin(a,b):
  if(a <= b):
    return a
  else:
    return b

def chmax(a,b):
  if(a >= b):
    return a
  else:
    return b


n,k = map(int,input().split())
h = list(map(int,input().split()))
INF = sum(h)+100

dp = [INF for i in range(n)]

dp[0] = 0

for i in range(1,n):
  for j in range(max(0,i-k),i):
    dp[i] = chmin(dp[i],dp[j]+abs(h[j] - h[i]))

print(dp[n-1])
