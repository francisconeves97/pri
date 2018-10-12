import operator
from ex3 import dot_product

print("Enter query: ")
terms = input().split(' ')

scores = dot_product(terms)

sorted_by_value = sorted(scores.items(), key=lambda kv: kv[1])

print(sorted_by_value)