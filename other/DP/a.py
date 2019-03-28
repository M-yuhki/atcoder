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


n = int(input())
h = list(map(int,input().split()))
INF = sum(h)+100

dp = [INF for i in range(n)]

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(n-2):
  dp[i+2] = chmin(dp[i] + abs(h[i]-h[i+2]),dp[i+1] + abs(h[i+1] - h[i+2]))

print(dp[n-1])
