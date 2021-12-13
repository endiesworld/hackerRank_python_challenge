def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def sum_of_factorial(digits):
    sum_of_fac = 0
    for i in digits:
        sum_of_fac += factorial(int(i))
    return sum_of_fac


def g(i):
    f_list = [{n: factorial(n)} for n in range(1, i + 1)]
    return f_list


print(g(5))
