import math
from ex1 import file_inverted_index

num_docs, inverted_index = file_inverted_index('lusiadas.txt')

print('Total number of documents: {}'.format(num_docs))

terms = 0
individual_terms = 0
for key in inverted_index:
  _, count = inverted_index[key]
  if count == 1:
    individual_terms += 1
  else:
    terms += count

print('Total number of terms: {}'.format(terms))
print('Total number of individual terms: {}'.format(individual_terms))

print('Insert terms to get statistics: ')
terms = input().split(' ')

for term in terms:
  if term in inverted_index:
    doc_occurrences, _ = inverted_index[term]
    doc_occurrences_count = len(doc_occurrences)
    df = doc_occurrences_count / num_docs
    print('Statistics for {}'.format(term))
    print('DF: {}'.format(df))

    max_occ = 0
    min_occ = 9999

    for doc in doc_occurrences:
      nmr_occ = len(doc_occurrences[doc])

      if nmr_occ > max_occ:
        max_occ = nmr_occ
      if nmr_occ < min_occ:
        min_occ = nmr_occ

    print('Max TF: {}, Min TF: {}'.format(max_occ, min_occ))

    idf = math.log10(num_docs / doc_occurrences_count)

    print('IDF: {}'.format(idf))


  else:
    print('The term {} doesn\'t exist in any document'.format(term))

  print()
  print()