from scipy.special import comb

n = int(input())

s = input()

Q = pow(10,9) + 7

p = -1
q = ""
r = ""
flg = True
for i in range(n):
  if(i%2 == 0):
    if(s[i] == s[2*n-i-1] == "B"):
      continue
    else:
      p = i
      q = s[i]
      r = s[2*n-i-1]
      break

  else:
    if(s[i] == s[2*n-i-1] == "W"):
      continue
    else:
      p = i
      q = s[i]
      r = s[2*n-i-1]
      break

if(p >= 0):
  for i in range(p,n):
    if(s[i] == q and s[2*n-i-1] == r):
      continue
    else:
      flg = False
      break

if(not(flg)):
  print(0)

else:
  bnum = s.count("B")
  wnum = 2*n - bnum
  print( int(comb(bnum,2))%Q * int(comb(wnum,2))%Q * n * 2%Q  )
