s = input().rstrip().split()
n = int(s[0])
a = int(s[1])
b = int(s[2])

count = 0
for i in range(1, n + 1):
    s = str(i)
    t = list(map(int, list(s)))
    x = sum(t)

    if(a <= x and x <= b):
        count += i
print("{}".format(count))
