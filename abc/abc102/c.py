n = int(input())
a = list(map(int,input().split()))

for i in range(n):
  a[i] -= (i + 1)


a.sort()

if(n%2 == 1):
  b = a[int(n/2)]

else:
  t = 0
  for i in a:
    t += abs(i)
  ave = t/n

  p = int(n/2)
  if(abs(a[p] - ave) <= abs(a[p-1] -ave)):
    b = a[p]
  else:
    b = a[p-1]

k = list(map(lambda x:abs(x-b),a))

print(sum(k))
