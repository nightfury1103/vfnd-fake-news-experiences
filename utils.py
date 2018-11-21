import ast, os

"""
load_n_gram(corpus_path): load data from corpus_path
"""
def load_n_gram(corpus_path):
    with open(corpus_path, encoding = 'utf-8') as file:
        words = file.read()
        words = ast.literal_eval(words)
        return words

