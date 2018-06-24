import math

s = input().rstrip().split()

n = int(s[0])
k = int(s[1]) - 1

a = input()

block = math.ceil(n / k)
if(k == 1):
    print(n - 1)
elif(n % k == 1):
    print(block - 1)
elif(n == k + 1):
    print(1)
else:
    print(block)
