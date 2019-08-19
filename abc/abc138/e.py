s = input()
t = input() # 逆向き

p = 0
b = len(s) - 1
c = 0
flg = True
for i in t:
  while True:
    if(i == s[p]):
      b = p
      p += 1
      if(p == len(s)):
        c += 1
        p = 0
      break  

    elif(b == p):
      flg = False
      break

    p += 1
    if(p == len(s)):
      p = 0
      c += 1
  
  if(not(flg)):
    break
if(flg):
  print(c*len(s) + p)
else:
  print(-1)
