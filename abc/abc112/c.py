n = int(input())
s = []

for i in range(n):
  s.append(list(map(int,input().split())))

ans_x = -1
ans_y = -1
ans_h = -1

for i in s:
  if(i[2] > 0):
    check_x,check_y,check_h = i
    break

for x in range(101):
  for y in range(101):
    flg = True
    H = check_h + abs(check_x - x) + abs(check_y - y)
    if(H <= 0):
      flg = False
      break

    else:
      for i in range(n):
        h = max( ( H - abs(s[i][0] - x) - abs(s[i][1] - y) ) ,0) 
        if(h != s[i][2]):
          flg = False
          break
    if flg:
      ans_y = y
      ans_h = H
      break

  if flg:
    ans_x = x
    break

print("{} {} {}".format(ans_x,ans_y,ans_h))
