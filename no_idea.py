n_m = input().split(" ")
i_input = set(input().split(" "))
a_input = set(input().split(" "))
b_input = set(input().split(" "))
len_set_i_input = len(i_input)
not_happy_in_happiness = a_input - i_input
not_sad_in_sadness = b_input - i_input
a_b_len = int(n_m[1])
happiness_level = a_b_len - len(not_happy_in_happiness)
sadness_level = a_b_len - len(not_sad_in_sadness)
print(happiness_level - sadness_level)

