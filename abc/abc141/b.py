s = input()

flg = True
for i in range(len(s)):
  if( ( (i%2==0) and (s[i] == "L") ) or ( (i%2==1) and (s[i] == "R"))):
    flg = False
    break

if(flg):
  print("Yes")
else:
  print("No")


