"""
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
"""

"""
ask
You are given a string .
Your task is to find the indices of the start and end of string  in .

Input Format

The first line contains the string .
The second line contains the string .

Constraints



Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input
    "aaadaa"
    "aa"
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
input_1 = input()
input_2 = input()
start = 0
end = len(input_1)
str_len = len(input_2)

result = []

while((start + str_len) <= end):
    stop = start+str_len
    if(input_1[start:stop] == input_2):
        result.append((start, stop - 1))
    start += 1

if len(result) > 1:
    for data in result:
        print(data)
else:
    print((-1, -1))
