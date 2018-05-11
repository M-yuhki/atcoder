 
n = int(input())
s = []
for i in range(n):
  s.append(int(input()))
s.sort(reverse=True)

count = 1
now = s[0]

for i in range(n - 1):
  if(s[i+1] < now):
    now = s[i+1]
    count += 1
  else:
    continue

print(count)
