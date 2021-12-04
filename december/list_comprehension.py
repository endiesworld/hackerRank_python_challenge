def lis_comprehension():
    x = 1
    y = 1
    z = 2
    n = 3
    general_lst = [[i, j, k]
                   for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    print(general_lst)


lis_comprehension()
# general_lst = []
# n_list = []
# for i in list(range(x+1)):
#     for j in list(range(y+1)):
#         for k in list(range(z+1)):
#             general_lst.append([i, j, k])
# for i in general_lst:
#     if((i[0] + i[1] + i[2] != n)):
#         n_list.append(i)
