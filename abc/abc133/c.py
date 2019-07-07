l,r = map(int,input().split())
diff = r - l

if(diff >= 2019):
  print(0)
else:
  lmod = l % 2019
  rmod = r % 2019
  if(rmod  < lmod):
    print(0)
  else:
    ans =2020
    for i in range(l,r+1):
      for j in range(i+1,r+1):
        if((i*j) % 2019 < ans):
          ans = (i*j) % 2019
    print(ans)

