import math
n = int(input())
if(n%2==0):
  print(int(math.pow(int(n/2),2)))
else:
  print(int(n/2) * int((n+1)/2))
