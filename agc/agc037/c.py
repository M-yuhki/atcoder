import statistics
import math
n=int(input())
r = []
g = []
b = []
s = input()
K = 998244353
for i in range(3*n):
  if(s[i] == "R"):
    r.append(i+1)
  elif(s[i] == "G"):
    g.append(i+1)
  else:
    b.append(i+1)

rgb = []
for i in range(n):
  rgb.append( [r[i],g[i],b[i]] )

ma = 3*n + 1
me = 0
mi = -1
mai = rgb[0].index( max(rgb[0]) )
mei = rgb[0].index( statistics.median(rgb[0]) )
mii = rgb[0].index( min(rgb[0]) )
c = 0
ans = 1
maf = True
mef = True
mif = True 
tf = True
for i in rgb:
  me_n = statistics.median(i)
  mai_n = i.index( max(i) )
  mei_n = i.index( me_n )  
  mii_n = i.index( min(i) )
  if(mi < me_n < ma and mai_n == mai and mei_n == mei and mii_n == mii):
    c += 1
    ma = max(i)
    me = me_n
    mi = min(i)
    if(mai_n != mai):
      maf = False
    if(mei_n != mei):
      mef = False
    if(mii_n != mii):
      mif = False
    mai = mai_n
    mei = mei_n
    mii = mii_n
  else:
    tf = False
    s = 0
    if(maf):
      s += 1
    if(mef):
      s += 1
    if(mif):
      s += 1
    if(c == 0):
      s = 0
    ans = ans * int( math.pow( math.factorial(c), s ) ) % K
    ma = max(i)
    me = me_n
    mi = min(i)
    mai = mai_n
    mei = mei_n
    mii = mii_n
    maf = True
    mif = True
    mef = True
    if(s == 0):
      c = 0

s = 0
if(maf):
  s += 1
if(mef):
  s += 1
if(mif):
  s += 1
if(tf):
  ans = ans * int(math.pow(  math.factorial(max(c,1)) , s)) % K
else:
  ans = ans * int(math.factorial(n)) % K

print(ans)

