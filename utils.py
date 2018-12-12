import ast, os

"""
load_n_gram(corpus_path): load data from corpus_path
"""
def load_n_gram(corpus_path):
  with open(corpus_path, encoding = 'utf-8') as file:
    words = file.read()
    words = ast.literal_eval(words)
    return words

"""
load_stopwords: load stopwords from 'stopwords.txt' file
Output: Set of stopwords
Stopwords.txt description: 1 word 1 line + 2 python style commments
"""
def load_stopwords(stopwords_path):
  words = set()
  with open(stopwords_path, encoding='utf-8') as file:
    for line in file:
      li=line.strip()
      if not li.startswith("#"):
        words.add(line.rstrip())
              
  return words
