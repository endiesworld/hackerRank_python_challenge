#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(a):
    # Write your code here
    # arr_len = len(a)
    # for index in range(0, arr_len):
    #     if(index >= (arr_len)/2):
    #         break
    #     elem_1 = a[index]
    #     elem_2 = a[(index * -1) - 1]
    #     a[(index * -1) - 1] = elem_1
    #     a[index] = elem_2
    print(list(reversed(a)))
    return a[: : -1]


if __name__ == '__main__':
    

    # arr_count = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    
    res = reverseArray([1,2,3,4,5])
    res = reverseArray("Okoro")
    print(res)
