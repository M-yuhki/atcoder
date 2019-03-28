n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n):
    total += a[i]

tar = total / n

d = tar
ans = 0
for i in range(n):
    k = abs(tar - a[i])
    if(k < d):
        d = k
        ans = i

print(ans)
