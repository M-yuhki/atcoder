s = input()
print(s)
flg = 0

while len(s) > 0:
  head=s[0]
  if(head == "d"):
    ren = s[0:5]
    if(ren != "dream"):
      flg = 1
      break
    elif(ren == "dream" and len(s) > 7):
      if(s[5:7]=="er"):
        s = s[7:]
      else:
        s = s[5:]
    else:
      s = s[5:]
  elif(head == "e"):
    ren = s[0:5]
    if(ren != "erase"):
      flg = 1
      break
    elif(ren == "erase" and len(s) > 6):
      if(s[5] == "r"):
        s = s[6:]
      else:
        s = s[5:]
    else:
      s = s[6:]  
  else:
    flg = 1
    break

if(flg == 1):
  print("No")
else:
  print("Yes") 
