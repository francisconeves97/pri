import nltk


text = ''

with open('text.txt') as f:
    text = f.read()

text_array1 = nltk.word_tokenize(text)

with open('text2.txt') as f:
    text = f.read()

text_array2 = nltk.word_tokenize(text)


common_words = list(set(text_array1).intersection(text_array2))

print('Common words: {}'.format(common_words))
print('{} words in common.'.format(len(common_words)))