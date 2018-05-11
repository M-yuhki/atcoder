s = input().rstrip().split()
n = int(s[0])
y = int(s[1])

x10 = -1
x5 = -1
x1 = -1

need10=0;
need5=0;
need1=0;

for i in range(int(y/10000)+1):
  for j in range(int((y-10000*i)/5000)+1):
    k = n - (i+j)
    if(i*10000+j*5000+k*1000 == y):
      x10 = i
      x5 = j
      x1 = k
      break
  else:
    continue
  break
print("{} {} {}".format(x10,x5,x1))
    
