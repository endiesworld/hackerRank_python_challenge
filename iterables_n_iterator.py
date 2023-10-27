from itertools import combinations

str_len = int(input().strip())
main_str = input().strip()
main_str = main_str.split(' ')
main_str = ''.join(main_str)
r = int(input().strip())

print(f" str_len: {str_len}")
print(f" main_str: {main_str}")
print(f" r: {r}")

tuple_list = list(combinations(main_str, r))
print(f" tuple_list : {tuple_list}")

len_tuple_list = len(tuple_list)
a_count = 0

for i_tuple in tuple_list:
    if "a" in i_tuple:
        a_count += 1

print(round((a_count/len_tuple_list), 4))
