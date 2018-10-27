n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
a.sort()
ans = 0

p = 0
q = n-1

if(n == 2):
  ans = a[q] - a[p]
else:
  ans += a[q] - a[p]
  for i in range(n-3):
    if(i % 2 == 0):
      ans += a[q] - a[p+1]
    else:
      ans += a[q-1] - a[p]
      p += 1
      q -= 1
  s = a[q] - a[p+1]
  t = a[q-1] - a[p]
  if(s >= t):
    ans += s
  else:
    ans += t

print(ans)


