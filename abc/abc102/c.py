n = int(input())
a = list(map(int, input().split()))

p = a[0]
q = 0

now_len = 1
max_len = 1
max_p = p
max_q = 0
total = p

for i in range(n - 1):
    total += a[i + 1]
    t = a[i + 1] - a[i]
    if(t == 1):
        now_len += 1
    else:
        if(max_len < now_len):
            max_len = now_len
            max_p = p
            max_q = q
        now_len = 1
        p = a[i + 1]
        q = i + 1

if(max_len < now_len):
    max_len = now_len
    max_p = p
    max_q = q

ans = 0

b = max_p - max_q
if(max_p == a[0] and max_len == 1):
    b = int(total / n) - int(n / 2)

for i in range(n):
    ans += abs(a[i] - (b + i))

print(ans)
