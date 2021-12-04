def lis_comprehension():
    x = 1
    y = 1
    z = 2
    n = 3
    general_lst = []
    # n_list = []
    for i in list(range(x+1)):
        for j in list(range(y+1)):
            for k in list(range(z+1)):
                general_lst.append([i, j, k])
    # for i in general_lst:
    #     if((i[0] + i[1] + i[2] != n)):
    #         n_list.append(i)
    n_list = [x for x in general_lst if sum(x) != n]
    print(n_list)


lis_comprehension()
# the_list = []
# for i in list(range(2)):
#     the_list.append(i)
# print(the_list)
