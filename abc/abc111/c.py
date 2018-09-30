import collections
n = int(int(input())/2)
a = list(map(int,input().split()))
o = []
e = []
for i in range(n):
  o.append(a[i*2])
  e.append(a[i*2+1])
o_c = collections.Counter(o)
e_c = collections.Counter(e)
o_most = o_c.most_common()[0][0]
o_num = o_c.most_common()[0][1]
e_most = e_c.most_common()[0][0]
e_num = e_c.most_common()[0][1]
ans = 0
if(o_most == e_most and o_num + e_num == n*2):
  ans = n
elif(o_most != e_most and o_num == n and e_num == n):
  ans = 0
else:
  if(o_most == e_most):
    if(len(o_c.most_common()) == 1):
      e_num = e_c.most_common()[1][1]
    elif(len(e_c.most_common()) == 1):
      o_num = o_c.most_common()[1][1]
    else:
      e_t = e_c.most_common()[1][1]
      o_t = o_c.most_common()[1][1]
      if(o_num - o_t <= e_num - e_t):
        o_num = o_t
      else:
        e_num = e_t
  ans = n*2 - o_num - e_num
print(ans)
