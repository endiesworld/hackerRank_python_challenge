
# Time out Error

"""
#word = 'BANANA'
#word = 'BANANANAAAS'
word = 'BAANANAS'
word_len = len(word)
sub_string = []
player_1 = {
    'name': 'Stuart',
    'score': 0
}

player_2 = {
    'name': 'Kevin',
    'score': 0
}
vowels = ['A', 'E', 'I', 'O', 'U']

for index in range(word_len):
    n = index
    while (n < word_len):
        n += 1
        sub_string.append(word[index: n])

for sub in sub_string:
    if(sub[0] in vowels):
        player_2['score'] += 1
    else:
        player_1['score'] += 1
if (player_1['score'] > player_2['score']):
    winner = player_1['name'] + ' ' + str(player_1['score'])
elif (player_1['score'] < player_2['score']):
    winner = player_2['name'] + ' ' + str(player_2['score'])
else:
    winner = 'Draw'
print(winner)
"""


# Time Limit Error Code
"""
word = 'BAANANAS'
word_len = len(word)
sub_string = []
player_1 = {
    'name': 'Stuart',
    'score': 0
}

player_2 = {
    'name': 'Kevin',
    'score': 0
}
vowels = ['A', 'E', 'I', 'O', 'U']

for index in range(word_len):
    n = index
    while (n < word_len):
        n += 1
        new_word = word[index: n]
        if(new_word[0] in vowels):
            player_2['score'] += 1
        else:
            player_1['score'] += 1

        #sub_string.append(word[index: n])

# for sub in sub_string:
#     if(sub[0] in vowels):
#         player_2['score'] += 1
#     else:
#         player_1['score'] += 1
if (player_1['score'] > player_2['score']):
    winner = player_1['name'] + ' ' + str(player_1['score'])
elif (player_1['score'] < player_2['score']):
    winner = player_2['name'] + ' ' + str(player_2['score'])
else:
    winner = 'Draw'
print(winner)

"""

# Still timed Out*****
"""
word = 'BAANANAS'
word_len = len(word)
sub_string = []
player_1 = {
    'name': 'Stuart',
    'score': 0
}

player_2 = {
    'name': 'Kevin',
    'score': 0
}
vowels = ['A', 'E', 'I', 'O', 'U']
for index, char in enumerate(word):
    n = index
    new_word = word[index:]
    if(new_word[0] in vowels):
        player_2['score'] += len(new_word)
    else:
        player_1['score'] += len(new_word)
if (player_1['score'] > player_2['score']):
    winner = player_1['name'] + ' ' + str(player_1['score'])
elif (player_1['score'] < player_2['score']):
    winner = player_2['name'] + ' ' + str(player_2['score'])
else:
    winner = 'Draw'
print(winner)

"""

# Passed all time complexity test.
word = 'BAANANAS'
word_len = len(word)
sub_string = []
player_1 = {
    'name': 'Stuart',
    'score': 0
}

player_2 = {
    'name': 'Kevin',
    'score': 0
}
vowels = ['A', 'E', 'I', 'O', 'U']
for index, char in enumerate(word):
    n = index
    new_word_len = word_len - index
    if(char in vowels):
        player_2['score'] += new_word_len
    else:
        player_1['score'] += new_word_len
if (player_1['score'] > player_2['score']):
    winner = player_1['name'] + ' ' + str(player_1['score'])
elif (player_1['score'] < player_2['score']):
    winner = player_2['name'] + ' ' + str(player_2['score'])
else:
    winner = 'Draw'
print(winner)
