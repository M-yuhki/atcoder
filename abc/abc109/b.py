n = int(input())
log = []
b = input()
log.append(b)
flg = True
for i in range(n-1):
  w = input()
  if(b[-1:] != w[0] or w in log):
    flg = False
    break
  else:
    log.append(w)
    b = w
if(flg):
  print("Yes")
else:
  print("No")

    
