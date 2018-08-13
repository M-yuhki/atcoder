
def check(x,y,li,z,s):
  ans = s
  p = li[x]
  y += p
  if(x == len(li) - 1):
    if(y % z == 0):
      ans += 1
  elif(y % z == 0):
    ans += check(x+1,y,li,z,ans)
  return ans
  
n,m = map(int,input().split())
a = map(int,input().split())
b = list(map(lambda x:x%m,a))
print(b)
ans = check(0,0,b,m,0)

print(ans)
