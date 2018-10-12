from ex1 import file_inverted_index
from ex2 import term_statistics

def dot_product(terms):
  num_docs, inverted_index = file_inverted_index('lusiadas.txt')
  a = {}
  for term in terms:
    inverted_dict = inverted_index[term][0]
    _, _, _, idf = term_statistics(term)

    for doc in inverted_dict:
      if doc not in a:
        a[doc] = 0
      a[doc] = a[doc] + len(inverted_dict[doc]) * idf

  return a