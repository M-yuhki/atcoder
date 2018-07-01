n = int(input())-1
a = list(map(int,input().split()))

a_max = a[0]
a_min = a[0]

for i in range(n):
  if(a_max < a[i+1]):
    a_max = a[i+1]
  if(a[i+1] < a_min):
    a_min = a[i+1]

print(a_max - a_min)


