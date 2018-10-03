# 2.2
import nltk


text = ''

with open('text.txt') as f:
    text = f.read().split()

syntactic_classes = nltk.pos_tag(text)


syntactic_dict = {}

for _, syntactic_class in syntactic_classes:

    if syntactic_class in syntactic_dict:
        syntactic_dict[syntactic_class] += 1
    else:
        syntactic_dict[syntactic_class] = 1

for syntactic_class in syntactic_dict:
    print('Syntactic class: {}, Occurences: {}'.format(syntactic_class, syntactic_dict[syntactic_class]) ) 