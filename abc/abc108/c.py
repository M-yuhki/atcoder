import math
n, k = map(int, input().split())
a = int(n/k)
if(a < 2):
    b = 0
else:
    b = math.factorial(a) // (math.factorial(a - 2) * 2)
if(a < 3):
    c = 0
else:
    j = math.factorial(a-3)
    c = math.factorial(a) // j * 6
ans = a + b * 6 + c * 6
if(k % 2 == 0):
    t = int(k / 2)
    if(a * k + t > n):
      ans = ans * 2
    else:
      d = a + 1
      if(d < 2):
          e = 0
      else:
          e = math.factorial(d) // j * 2)
      if(d < 3):
          f = 0
      else:
          f = math.factorial(d) // (math.factorial(d - 3) * 6)
      ans += (d + e * 6 + f * 6)
print(ans)
