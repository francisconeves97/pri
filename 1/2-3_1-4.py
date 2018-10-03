# 2.3 - 1.4
from sklearn.feature_extraction.text import TfidfVectorizer


texts = []

with open('text.txt') as f:
    texts.append(f.read())

with open('text2.txt') as f:
    texts.append(f.read())

vectorizer = TfidfVectorizer()


counts = vectorizer.fit_transform(texts)
words = vectorizer.get_feature_names()

