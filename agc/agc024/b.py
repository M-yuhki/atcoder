n = int(input())

top = int(input())
l = 0
lr = 0
pl = top
r = 0
rl = 0
pr = top 

for i in range(n - 1):
  s = int(input())
  if(s < top):
    l += 1
    if(s < pl):
      pl = s
    else:
      lr += 1
  else:
    r += 1
    if(pr < s):
      pr = s
    else:
      rl += 1

a = rl*2 + l
print(a)
