# 2.3 - 1.3
from sklearn.feature_extraction.text import CountVectorizer


text = []

with open('text.txt') as f:
    text = [f.read()]

vectorizer = CountVectorizer()


counts = vectorizer.fit_transform(text)
words = vectorizer.get_feature_names()

for i in range(len(words)):
    print('Word: {}, Occurrences: {}'.format(words[i], counts[0, i]))