# PROBLEM
"""
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.
"""
# ASSUMPTIONS:
"""
The number query occurs somewhere in the middle of the list cards.
query is the first element in cards.
query is the last element in cards.
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.
"""

# TEST CASES FOR ASSUMPTIONs :
tests = []
# query occurs in the middle
tests.append({"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3})

tests.append({"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6})

# query is the first element
tests.append({"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0})

# query is the first element
tests.append({"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0})

# query is the last element
tests.append({"input": {"cards": [3, -1, -9, -127], "query": -127}, "output": 3})

# cards contains just one element, query
tests.append({"input": {"cards": [6], "query": 6}, "output": 0})

# We will assume that our function will return -1 in case cards does not contain query.
# cards does not contain query
tests.append({"input": {"cards": [9, 7, 5, 2, -9], "query": 4}, "output": -1})

# cards is empty
tests.append({"input": {"cards": [], "query": 7}, "output": -1})

# numbers can repeat in cards
tests.append(
    {
        "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 3},
        "output": 7,
    }
)

# query occurs multiple times
tests.append(
    {
        "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 6},
        "output": 2,
    }
)

# Solution(1)
# 1.1 Algorithm: Linear Search
# 1.2 Complexity: O(N)
print(f"You have {len(tests)} numbers of test cases")


def loacate_query(cards, query):
    query_location = -1
    for index, card in enumerate(cards):
        if card == query:
            query_location = index
            break
    return query_location


print("*** Test case with Linear Search Algorith ***")
print(loacate_query(**tests[0]["input"]) == tests[0]["output"])

# Solution(2)
# 2.1 Algorithm: Binary Search
# 2.2 Complexity:


# def locate_card(cards, query):
#     lo, hi = 0, len(cards) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2
#         mid_number = cards[mid]

#         print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

#         if mid_number == query:
#             return mid
#         elif mid_number < query:
#             hi = mid - 1
#         elif mid_number > query:
#             lo = mid + 1

#     return -1


# Binary Search update: To return first index for a search


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1


print("*** Test case with Binary Search Algorithm ***")

for i in range(len(tests)):
    print(loacate_query(**tests[i]["input"]) == tests[i]["output"])
