n = int(input())

flg = False

for i in range(26):
  t = n - i*4
  if(t < 0):
    break
  elif(t == 0):
    flg = True
    break
  else:
    if(t % 7 == 0):
      flg = True
      break

if(flg):
  print("Yes")
else:
  print("No")
