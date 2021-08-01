from pprint import pprint
sentence = "This is a common question"
char_dict = {}
for char in sentence:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1
sort = sorted(char_dict.items(), key=lambda kv: kv[1], reverse=True)
pprint(sort)
