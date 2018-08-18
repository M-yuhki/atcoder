def check(s):
  a = len(s)
  x = False
  if(a == 0):
    x = True
  elif(a == 5):
    if(s == "dream" or s == "erase"):
      x = True
  elif(a == 6):
    if(s == "eraser"):
      x = True
  elif(a == 7):
    if(s == "dreamer"):
      x = True
  elif(a > 9):
    if(s[-5:] == "dream" or s[-5:] == "erase"):
      x = check(s[:-5])
    elif(s[-6:] == "eraser"):
      x = check(s[:-6])
    elif(s[-7:] == "dreamer"):
      x = check(s[:-7])
  return x

s = input()

if(check(s)):
  print("YES")
else:
  print("NO")


