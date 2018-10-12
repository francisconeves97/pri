import nltk

def file_inverted_index(filename):
  with open('lusiadas.txt', encoding='ISO-8859-1') as f:
    text_lines = f.readlines()

  text_lines = [nltk.word_tokenize(line) for line in text_lines if line != '\n']

  inverted_index = {}

  for i in range(len(text_lines)):
    line = text_lines[i]

    for j in range(len(line)):
      word = line[j]
      if word in inverted_index:
        occurences = inverted_index[word][0]
        if i in occurences:
          occurences[i].append(j)
        else:
          occurences[i] = [j] 

        inverted_index[word][1] += 1
      else:
        inverted_index[word] = []
        inverted_index[word].append({i: [j] })
        inverted_index[word].append(1)

  return len(text_lines), inverted_index
