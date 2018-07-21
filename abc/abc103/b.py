s = input()
t = input()
flg = False
x = len(s)
for i in range(x):
  k = s[i:] + s[:i]
  if(k == t):
    flg = True
    break
if(flg):
  print("Yes")
else:
  print("No")
