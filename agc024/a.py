s = input().rstrip().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
k = int(s[3])

ans = a - b

if(k%2==1):
  ans = -1 * ans

if(abs(ans) < 1000000000000000000):
  print(ans)
else:
  print("Unfair")
