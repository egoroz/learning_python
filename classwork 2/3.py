# дефолтные значения
# n, m = 5, 6

#1
#[[j*m+i for i in range(m)]for j in range(n)]


#2
#[[0 if i == j else 1 if i>j else 2 for i in range(m)] for j in range(n)]


#3
#[[i if i>=j else j for i in range(n)] for j in range(n)]


#4
# with open('input.txt','r') as file:
#     file = file.readlines()
#     for line in file[::-1]:
#         print(line,end = '')


#5
# with open('input.txt', 'r') as file:
#     file = file.read()
#     print(file[::-1])


#6
# with open('input.txt', 'r') as f:
#     W9, W10, W11 = 0, 0, 0
#     file = f.readline().split()
#     while len(file)>0:
#         if file[2] == '9' and int(file[3])>W9:
#             W9 = int(file[3])
#         if file[2] == '10' and int(file[3])>W10:
#             W10 = int(file[3])
#         if file[2] == '11' and int(file[3])>W11:
#             W11 = int(file[3])
#         file = f.readline().split()
#     print(W9,W10,W11)



#7
# with open('input.txt', 'r') as f:
#     possible_winners = []
#     now_max = 0
#     line = f.readline().split()
#     while len(line) > 0:
#         if int(line[3]) > now_max:
#             now_max = int(line[3])
#             possible_winners = [line[2]]
#         elif int(line[3]) == now_max:
#             possible_winners.append(line[2])
#         line = f.readline().split()
# possible_winners.sort()
# winners = []
# for el in possible_winners:
#     if el not in winners:
#         winners.append(el)
# print(winners)


#8
# with open('input.txt','r') as f:
#     f = f.readlines()
#     line = list(map(lambda x: x.split(), f))
#     line.sort()
# for i in range(len(line)):
#     print(line[i][0], line[i][1], line[i][3])


#9
# with open('input.txt','r') as f:
#     f = f.readlines()
#     f = list(map(lambda x: x.split(), f))
#     S9,S10,S11,k9,k10,k11 = [0]*6
#     for arr in f:
#         if arr[2] == '9':
#             S9 += int(arr[3])
#             k9 += 1
#         elif arr[2] == '10':
#             S10 += int(arr[3])
#             k10 += 1
#         else:
#             S11 += int(arr[3])
#             k11 += 1
# print(S9/k9,S10/k10,S11/k11)