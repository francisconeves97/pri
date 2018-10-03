import nltk


text = ''

with open('text.txt') as f:
    text = f.read()

text_array = nltk.word_tokenize(text)

word_dict = {}
for word in text_array:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word in word_dict:
    print('Word: {}, Occurences: {}'.format(word, word_dict[word]) ) 