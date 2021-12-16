n_m = input().split()
i_input = input().split()
a_input = set(input().split())
b_input = set(input().split())
hapines_set = 0
for i in i_input:
    if i in a_input:
        hapines_set += 1
    elif i in b_input:
        hapines_set += -1
print(hapines_set)

