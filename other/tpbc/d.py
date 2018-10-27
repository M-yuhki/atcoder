import copy
n = int(input())
if(n == 3 or n%4 == 2):
  print("Yes")
  if(n == 3):
    print("2 1 2")
    print("2 3 2")
    print("2 1 3")
  else:
    s = int((n+2)/4) - 1 #余分の数
    t = 2 + s #最初の3の数
    print(3+s) #集合の総数
    a = list(range(1,t+1))
    b = list(map(lambda x:x+t-1,a))
    c = list(map(lambda x:x+t-1,b))
    x = c[len(c) - 1]
    c[len(c)-1] = 1
    k = (' '.join(map(str, a)))
    print("{} {}".format(t,k))
    k = (' '.join(map(str, b)))
    print("{} {}".format(t,k))
    k = (' '.join(map(str, c)))
    print("{} {}".format(t,k))
    
    z = list(range(x,n+1))
    print(z)
    for i in range(s):
      w = copy.deepcopy(z)
      
      w.pop(i)
      o = ' '.join(map(str,w))      
      print("{} {} {} {} {}".format(3+len(z) -1,a[i+1],b[i+1],c[1+i],o))
else:
  print("No")
