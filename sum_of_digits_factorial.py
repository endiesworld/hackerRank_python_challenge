def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def f(n):
    f_n = 0
    str_digit = str(n)
    for i in str_digit:
        f_n += factorial(int(i))
    return f_n


def sf(n):
    n_str = str(f(n))
    s_f_n = 0
    for i in n_str:
        s_f_n += int(i)
    return s_f_n


def g(i):
    f_list = [{n: sf(n)} for n in range(1, i + 1)]
    return f_list


print(sf(12345))
print(sf(234))
# print(sf(25))
