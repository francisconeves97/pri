# 1.3

import re
import string

regex = re.compile('[%s]' % re.escape(string.punctuation))

text_array = []

with open('text.txt') as f:
    text_array = regex.sub(' ', f.read().lower()).split()

word_dict = {}
for word in text_array:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word in word_dict:
    print('Word: {}, Occurences: {}'.format(word, word_dict[word]) ) 