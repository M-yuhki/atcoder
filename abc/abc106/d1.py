n,m,q = map(int,input().split())
train = []
num = [[0,0] for i in range(n)]
for i in range(m):
  l,r = map(int,input().split())
  train.append([l,r])
  num[l-1][0] += 1

train.sort(key=lambda x:(x[0],x[1]))

for i in range(n-1):
  num[i+1][1] = num[i][0] + num[i][1]

for i in range(q):
  l,r = map(int,input().split())
  ans = 0
  for j in range(l,r+1):
    s = num[j-1][0]
    t = num[j-1][1]
    u = 0
    if(train[t+s-1][1] < r):
      ans += s
    else:
      for k in range(s):
        if(train[t+k][1] > r):
          u = s - k
          break
      ans += s - u
  print(ans)
