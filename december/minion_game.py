word = 'BANANA'
#word = 'BANANANAAAS'
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
