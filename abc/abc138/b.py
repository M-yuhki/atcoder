n = int(input())

a = list(map(int,input().split()))

a = list(map(lambda x: 1/x,a))

ans = 1/sum(a)

print(ans)
