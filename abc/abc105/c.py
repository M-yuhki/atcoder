import math
n = int(input())

if(n == 0):
  print("0")
else:
  s = ""
  if(n > 0):
    pm = True
  else:
    pm = False
  m = abs(n)
  k = 1
  l = 0
  while True:
    a = math.pow(4,k)
    if(a - l > m):
      break
    l += a
    k += 1
  # k*2が目安の桁数
  now = 0
  q = int(math.pow(4,k))
  for i in range(k):
    p = int(q)
    q = math.pow(4,k-i-1)
    c = int((p+q)/2)

