#!/bin/python3

"""_summary_

    Given a 6 x 6 2D Array, :
    An hourglass in A is a subset of values with indices falling in this pattern in 's graphical representation:
    a b c
      d
    e f g
    
    There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr,
    then print the maximum hourglass sum. The array will always be 6x6.

Example
    arr = 
    -9 -9 -9  1 1 1 
     0 -9  0  4 3 2
    -9 -9 -9  1 2 3
     0  0  8  6 6 0
     0  0  0 -2 0 0
     0  0  1  2 4 0
     
     The 16 hourglass sums are:
     -63, -34, -9, 12, 
     -10,   0, 28, 23, 
     -27, -11, -2, 10, 
     9,  17, 25, 18
     
     The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2 :

"""


import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    r_1_c_1 = [0, 0]
    r_1_c_2 = [0, 1]
    r_1_c_3 = [0, 2]

    r_2_c_2 = [1, 1]

    r_3_c_1 = [2, 0]
    r_3_c_2 = [2, 1]
    r_3_c_3 = [2, 2]

    result = []
    for row in range(0, 4):
        for col in range(0, 4):
            a = (arr[r_1_c_1[0] + row][r_1_c_1[1] + col] +
                 arr[r_1_c_2[0] + row][r_1_c_2[1] + col] +
                 arr[r_1_c_3[0] + row][r_1_c_3[1] + col] +
                 arr[r_2_c_2[0] + row][r_2_c_2[1] + col] +
                 arr[r_3_c_1[0] + row][r_3_c_1[1] + col] +
                 arr[r_3_c_2[0] + row][r_3_c_2[1] + col] +
                 arr[r_3_c_3[0] + row][r_3_c_3[1] + col])
            result.append(a)
    return max(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
