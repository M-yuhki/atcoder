s = input().rstrip().split()
t = list(map(lambda x:int(x),s))

if(abs(t[0] - t[2]) <=t[3] or (abs(t[0]-t[1]) <= t[3] and  abs(t[1] -t[2]) <= t[3])):
  print("Yes")
else:
  print("No")
