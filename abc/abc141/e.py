n = int(input())

s = input()

k = []

for i in range(n):
  k.append(s[n-i-1:])

list.sort(k)

abc = "abcdefghijklmnopqrstuvwxyz"
st = [-1 for i in range(26)]
en = [-1 for i in range(26)]

p = ""

for i in abc:
  if(i in k):
    s = k.index(i)
    if(p == "")
      st[p] = 0
      p = i
    else:
      en[p] = s-1
      st[]
