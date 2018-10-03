# 1.4

import re
import string

regex = re.compile('[%s]' % re.escape(string.punctuation))

text_array1 = []

with open('text.txt') as f:
    text_array1 = regex.sub(' ', f.read().lower()).split()

text_array2 = []

with open('text2.txt') as f:
    text_array2 = regex.sub(' ', f.read().lower()).split()

common_words = list(set(text_array1).intersection(text_array2))

print('Common words: {}'.format(common_words))
print('{} words in common.'.format(len(common_words)))