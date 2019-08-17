s = input()
ans = 0
p = ""
for i in s:
  p += i
  if(len(p) == 3):
    if(p[0] == p[1] == p[2]):
      ans += 1
      p = i
    elif(p[0] == p[1] and p[0] != p[2]):
      ans += 1
      p = i
    else:
      ans += 2
      p = i

if(len(p) == 2):
  if(p[0] == p[1]):
    ans += 1
  else:
    ans += 2

else:
  ans += 1

print(ans)

