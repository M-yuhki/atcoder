s = input()

p = len(s)
c = p

flg = True

while c > 0:
  tflg = True
  if(c <= 4):
    flg = False
    break

  if(c >= 7):
    tar = s[c-7:c]
    if(tar == "dreamer"):
      c -= 7
      tflg = False
  
  if(c >= 6):
    tar = s[c-6:c]
    if(tar == "eraser"):
      c -= 6
      tflg = False

  if(c >= 5):
    tar = s[c-5:c]
    if(tar == "dream" or tar == "erase"):
      c -= 5
      tflg = False

  if(tflg):
    flg = False
    break


if(flg):
  print("YES")
else:
  print("NO")






