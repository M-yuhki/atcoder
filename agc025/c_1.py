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
    s.append(i)
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

for i in range(n):
    if(field == 1):
        aoki = field1.pop(0)
        if(now < aoki[0] or aoki[1] < now):
            move += abs(now - aoki[target])
            now = aoki[target]
        del_key = aoki[2]
        for j in range(len(field2)):
            if(field2[j][2] == del_key):
                field2.pop(j)
                break
        field = 2

    else:
        aoki = field2.pop(0)
        if(now < aoki[0] or aoki[1] < now):
            move += abs(now - aoki[1 - target])
            now = aoki[1 - target]
        del_key = aoki[2]
        for j in range(len(field1)):
            if(field1[j][2] == del_key):
                field1.pop(j)
                break
        field = 1


print(move + abs(now))
