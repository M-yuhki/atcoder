a,b,c = map(int,input().split())

x = abs(a-b)
y = abs(b-c)
z = abs(c-a)

print(x+y+z-max(x,y,z))
