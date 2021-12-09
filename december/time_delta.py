from datetime import datetime, time
import math
import os
import random
import re
import sys

# Complete the time_delta function below.


def time_delta(t1, t2):
    return time.asctime()


t = int(input())

for t_itr in range(t):
    t1 = input()
    t2 = input()

    delta = time_delta(t1, t2)

    print(delta)
