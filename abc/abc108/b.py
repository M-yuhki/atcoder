import math
x1,y1,x2,y2=map(int,input().split())
r = int(math.sqrt(math.pow(abs(x1-x2),2) + math.pow(abs(y1-y2),2)))
mx = x2 - x1
my = y2 - y1
print("{} {} {} {}".format(x2-my,y2+mx,x2-my-mx,y2+mx-my))
