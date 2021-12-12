from datetime import datetime, time, timedelta, timezone

import math
import os
import random
import re
import sys

# Complete the time_delta function below.


def format_timezone(t_zone):
    sign = t_zone[0]
    time_int = t_zone[1] + t_zone[2]
    time_dec = t_zone[3] + t_zone[4]
    formated_timezone = [float(sign + time_int), float(sign + time_dec)]
    return formated_timezone


months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def time_delta(t1, t2):
    t1_prop = t1.split(" ")
    t2_prop = t2.split(" ")
    splited_time1 = t1_prop[4].split(":")
    splited_time2 = t2_prop[4].split(":")
    t1_prop[-1] = format_timezone(t1_prop[-1])
    t2_prop[-1] = format_timezone(t2_prop[-1])
    t1_time = datetime(
        int(t1_prop[3]),
        months[t1_prop[2]],
        int(t1_prop[1]),
        int(splited_time1[0]),
        int(splited_time1[1]),
        int(splited_time1[2]),
        tzinfo=timezone(timedelta(hours=t1_prop[-1][0], minutes=t1_prop[-1][1])),
    )
    t2_time = datetime(
        int(t2_prop[3]),
        months[t2_prop[2]],
        int(t2_prop[1]),
        int(splited_time2[0]),
        int(splited_time2[1]),
        int(splited_time2[2]),
        tzinfo=timezone(timedelta(hours=t2_prop[-1][0], minutes=t2_prop[-1][1])),
    )

    delta = t1_time - t2_time
    totalSec = int(delta.total_seconds())
    return str(abs(totalSec))


# t = int(input())

# for t_itr in range(t):
#     t1 = input()
#     t2 = input()

#     delta = time_delta(t1, t2)

#     print(delta)


my_date = time_delta("Fri 11 Feb 2078 00:05:21 +0400", "Mon 29 Dec 2064 03:33:48 -1100")
my_date2 = time_delta(
    "Wed 12 May 2269 23:22:15 -0500", "Tue 05 Oct 2269 02:12:07 -0200"
)
# print(
#     datetime(2015, 5, 2, 19, 54, 36, tzinfo=timezone(timedelta(hours=+5, minutes=30)),)
# )
print(my_date)
print(my_date2)

