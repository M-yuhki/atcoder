s = input().rstrip().split()
h = int(s[0])
w = int(s[1])

table = []

for i in range(h):
  t = input()
  line = list(t)
  table.append(line)

flg = 0

h_edge = h-1
w_edge = w-1

for i in range(h):
  for j in range(w):
    if(table[i][j] == "#"):
      table[i][j] == "/"
      if(i == 0 and j == 0):
        if(table[i][j+1] == "." and table[i+1][j] == "."):
          flg = 1
      elif(i == 0 and j != w_edge):
        if(table[i][j+1] == "." and table[i+1][j] == "." and table[i][j-1] == "."):
          flg = 1
      elif(j == 0 and i != h_edge):
        if(table[i][j+1] == "." and table[i+1][j] == "." and table[i-1][j] == "."):
          flg = 1
      elif(i == h_edge and j == w_edge):
        if(table[i-1][j] == "." and table[i][j-1] == "."):
          flg = 1
      elif(i == h_edge):
        if(table[i][j+1] == "." and table[i][j-1] == "." and table[i-1][j] == "."):
          flg = 1
      elif(j == w_edge):
        if(table[i+1][j] == "." and table[i][j-1] == "." and table[i-1][j] == "."):
          flg = 1
      else:
        if(table[i][j+1] == "." and table[i+1][j] == "." and table[i][j-1] == "." and table[i-1][j] == "."):
          flg = 1
      if(flg == 1):
        break
  else:
    continue
  break

if(flg==0):
  print("Yes")
else:
  print("No")
