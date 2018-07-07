import math

n, m, d = map(int, list(input().split()))
# これこれ
if(d == 0):
    total = m / n
else:
    l = 2 * d
    k = n - 2 * d

    s = 2 * k + l
    total = 0

    for i in range(m - 1):
        total += s / math.pow(n, i)

print("{:.11}".format(total))
