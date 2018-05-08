def pay500(a, b, c, x):
    s = int(x / 500)
    count = 0
    if(s == 0 or a == 0):
        count += pay100(b, c, x)
    else:
        t = min(s, a) + 1
        for i in range(t):
            count += pay100(b, c, x - i * 500)
    return count


def pay100(b, c, x):
    s = int(x / 100)
    count = 0
    if(s == 0 or b == 0):
        count += pay50(c, x)
    else:
        t = min(s, b) + 1
        for i in range(t):
            count += pay50(c, x - i * 100)
    return count


def pay50(c, x):
    s = int(x / 50)
    if(c >= s):
        return 1
    else:
        return 0


a = int(input())
b = int(input())
c = int(input())
x = int(input())

print("{}".format(pay500(a, b, c, x)))