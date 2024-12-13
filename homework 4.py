# n = str(input('Введите строку\n'))
# a = []
# f = ''
# for i in n:
#     if i == 'н' or i == 'n':
#         i = '!'
#         a.append(i)
#     else:
#         a.append(i)
# for j in a:
#     f += j
# print(f)

# n = str(input('Введите строку\n'))
# a = []
# f = ''
# n = n.split()
# print(n)
# check = 0
# count = 0
# for j in n:
#     for i in j:
#         if i == 'н':

# n = str(input())
# f = ''
# valve = 0
# for i in n:
#     if i == ')':
#         valve = 0
#     elif valve == 1:
#         f += i
#     elif i == '(':
#         valve = 1
#     else:
#         continue
# print(f)

# n = input()
# n = n.split()
# f = []
# for i in n:
#     if i[0] == 'а' and i[-1] == 'я':
#         f.append(i)
#     elif i[-1] == ',' or i[-1] == '.' or i[-1] == '!' or i[-1] == '?':
#         if i[0] == 'а' and i[-2] == 'я':
#             f.append(i[0:-1])
#         else:
#             continue
#     else:
#         continue
# print(f)