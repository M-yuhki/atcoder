s = input()
k = int(input())
a = 0 
b = 0
for i in range(len(s)):
  if(s[i] != "1"):
    a = s[i]
    b = i + 1
    break
if(a == 0 or k < b):
  print(1)
else:
  print(a)
