s = input()
k = int(input())

dic = []

for i in range(len(s)):
  for j in range(len(s) - i):
    dic.append(s[i:i+1+j])

dic_sort = sorted(list(set(dic)))
print(dic_sort[k-1])
