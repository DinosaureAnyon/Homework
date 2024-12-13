from random import randint
arr=list()
n=3
m=4
for i in range(n):
  arr.append([randint(0, 9) for x in range(m)])
for i in range(n):
  for j in range(m):
    print(arr[i][j], end = ' ')
  print()
s=0
for i in range(n):
  if sum([arr[i][j] for j in range(m)])>=s:
    s=sum([arr[i][j] for j in range(m)])
    st=arr[i]
print(st,s)



from random import randint
arr=list()
n=3
m=4
for i in range(n):
  arr.append([randint(10, 99) for x in range(m)])
for i in range(n):
  for j in range(m):
    print(arr[i][j], end = ' ')
  print()
for i in range(n):
  if min(arr[i])%2==0:
    arr[i][arr[i].index(min(arr[i]))]=0
  else:
    arr[i][arr[i].index(min(arr[i]))]=1
print()
for i in range(n):
  for j in range(m):
    print(arr[i][j], end = ' ')
  print()