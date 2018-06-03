n = int(input())

field1 = []
field2 = []

max_r = 0
max_l = 0

for i in range(n):
    s = list(map(int, list(input().rstrip().split())))
    if(max_r < s[0]):
        max_r = s[0]
    if(s[1] < max_l):
        max_l = s[1]
    field1.append(s)
    field2.append(s)

if(max_r >= -max_l):  # 最初の進行方向右
    target = 0
    field1.sort(key=lambda x: -x[0])
    field2.sort(key=lambda x: x[1])
else:
    target = 1
    field1.sort(key=lambda x: x[1])
    field2.sort(key=lambda x: -x[0])

move = 0
now = 0
field = 1
m = int(n / 2)

for i in range(m + 1):
    if(field1[i][0] <= now and now <= field1[i][1]):
        break
    last = field1[i][target]
    if(now > 0 and last > 0)or(now < 0 and last < 0):
        move += abs(now - last)
    else:
        move += abs(now) + abs(last)
    now = last
    if(i == m):
        break
    else:
        if(field2[i][0] <= now and now <= field2[i][1]):
            break
        last = field2[i][1 - target]
    if(now > 0 and last > 0)or(now < 0 and last < 0):
        move += abs(now - last)
    else:
        move += abs(now) + abs(last)
    now = last

move += abs(now)

print(move)
