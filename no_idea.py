
# n_m = input().split(" ")
# i_input = set(input().split(" "))
# a_input = set(input().split(" "))
# b_input = set(input().split(" "))
# len_set_i_input = len(i_input)
# hapines_set = a_input & i_input
# sadnes_set = b_input & i_input
# print(len(hapines_set) - len(sadnes_set))
# print(f'Happiness set: {hapines_set}')
# print(f'sadnes_set: {sadnes_set}')
# print(f'Attribute5 5')
# # not_happy_in_happiness = a_input - i_input
# # not_sad_in_sadness = b_input - i_input
# # a_b_len = int(n_m[1])
# # happiness_level = a_b_len - len(not_happy_in_happiness)
# # sadness_level = a_b_len - len(not_sad_in_sadness)
# # print(happiness_level - sadness_level)
# print(len(hapines_set) - len(sadnes_set))

n_m = input().split(" ")
i_input = set(input().split(" "))
a_input = input().split(" ")
b_input = input().split(" ")
hapy = 0
for i in range(int(n_m[1])):
    if a_input[i] in i_input:
        hapy += 1
    elif b_input in i_input:
        hapy += -1
print(hapy)
