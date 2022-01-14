from collections import deque

items = [1, 8, 2, 23, 7, 9]
"""
# UNPACKING & RETURN STATEMENT BASE ON CONDITION
# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head

# print(sum(items))
"""

"""
# yield-STATEMENT, PAUSING A FUNCTION ON ANY CALL
def simpleGeneratorFun(value):
    index = 0
    yield value, index
    index += 1
    yield value, index
    index += 1
    yield value, index
    index += 1
    yield value, index
    index += 1

# Driver code to check above generator function
start_value = 2
for value in simpleGeneratorFun(start_value):
    print(value)
    start_value += 2
    # print(simpleGeneratorFun(start_value))
    print([*simpleGeneratorFun(start_value)])
"""
"""
# PROBLEM : You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing.

my_deque_1 = deque(maxlen=3)
for i in range(10):
    my_deque_1.append(i)
    print(my_deque_1)

my_deque_2 = deque(maxlen=3)
for i in range(10):
    my_deque_2.appendleft(i)
    print(my_deque_2)

"""

