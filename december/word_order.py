num_words = int(input())
word_count = 0
words = []
word = ""
words_dict = {}
while word_count < num_words:
    char = input()
    if char == "\n":
        if word in words_dict:
            words_dict.word.count += 1
        else:
            words_dict[word]["word"] = word
            words_dict[word]["count"] = 1
        word_count += 1
        words.append(word)
        word = ""
    else:
        word += char
no_dist_words = len(words_dict)
print(no_dist_words)
for index, dict_key in words:
    if dict_key in words_dict:
        print(words_dict[dict_key].count, end=" ")
        del words_dict[dict_key]

