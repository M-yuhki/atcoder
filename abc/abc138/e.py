import bisect
import sys
sys.setrecursionlimit(10**7)

s = input()
t = input()

abc = "abcdefghijklmnopgrstuvwxyz"

p = {}

for i in abc:
  p[i] = []

for i in range(len(s)):
  p[s[i]].append(i)
  
for i in abc:
  p[i].sort()

l = 0
c = -1

flg = True

for i in t:
  tar = p[i]
  if(len(tar) == 0):
    flg = False
    break
  index = bisect.bisect_left(tar,c)

  if(index == len(tar)):
    index = 0
    l += 1

  elif(c == tar[index]):
    l += 1
  c = tar[index]


if(flg):
  print(l*len(s) + c + 1)

else:
  print("-1")
