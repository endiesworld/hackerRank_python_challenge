my_list = []


def insert(i, e):
    my_list.insert(i, e)


def remove(e):
    if e in my_list:
        my_list.remove(e)


def append(e):
    my_list.append(e)


def sort():
    my_list.sort()


def pop():
    my_list.pop()


def reverse():
    my_list.reverse()


# def print():
#     print(my_list)


activity_dic = {'insert': insert, 'remove': remove, 'append': append,
                'sort': sort, 'pop': pop, 'reverse': reverse}

N = int(input('Pls enter you number operation'))


def operation(n):
    activities = n.split(' ')
    if activities[0] == 'print':
        print(my_list)
    elif len(activities) == 3:
        activity_dic[activities[0]](int(activities[1]), activities[2])
    elif len(activities) == 2:
        activity_dic[activities[0]](activities[1])
    else:
        activity_dic[activities[0]]()


for i in range(N):
    n = input()
    operation(n)
