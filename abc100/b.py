s = input().rstrip().split()

n = int(s[1])

if(s[0] == "0"):
  if(n == 100):
    print(101)
  else:
    print(n)
elif(s[0] == "1"):
  if(n == 100):
    print(10100)
  else:
    print(100*n)
elif(s[0] == "2"):
  if(n == 100):
    print(1010000)
  else:
    print(10000*n)
