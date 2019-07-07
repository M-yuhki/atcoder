n = int(input())
a = list(map(int,input().split()))

ans = []
x = a[0]
y = a[0]
  
flg = False
for i in range(n-1):
   if flg:
     x += a[i+1]
     y -= a[i+1]
     flg = False
   else:
     x -= a[i+1]
     y += a[i+1]
     flg = True

ans.append(x)
ans.append(y)

p = 0

for i in range(n-2):
  ans.append(ans[p] -2*a[p] + 2*a[p+1] )
  p += 1

ans_str = " ".join(list(map(str,ans)))
print(ans_str)
