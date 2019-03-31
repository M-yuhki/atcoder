import string

n,q = map(int,input().split())
s = input()
a = 0
for i in range(n+0):
  a += pow(10,i)
a = a*10
d = [0 for i in range(26)]
k = 0
for i in string.ascii_uppercase:
  if(i in s):
    b = 0
    for j in range(n):
      if(s[j] == i):
        b += pow(10,n-j)
    d[k] = b
  k += 1

print("a {}".format(a))
print("d {}".format(d))

for i in range(q):
  t,u = map(str,input().split())
  v = d[ord(t) - 65]
  if(u == "L"):
    a = a + 9*v
  else:
    a = a - 9*v
  print(a)
  
