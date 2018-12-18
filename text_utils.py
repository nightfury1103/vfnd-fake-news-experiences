import unicodedata as ud
import sys

"""
  remove_punc: remove punctuation from text
  input:
    + text: String Type
  output: text after remove all punctuations
"""
def remove_punc(text):
  tbl = dict.fromkeys(i for i in range(sys.maxunicode)
                    if ud.category(chr(i)).startswith('P'))
  return text.translate(tbl)

"""
  remove_stopwords: remove "stopwords" from "paragraph"
  input: 
    + stopwords: Set() of stopwords
    + paragraph: List() of word in paragraph
  output: List() of words after remove stopwords
"""
def remove_stopwords(paragraph, stopwords):
  new_para = []
  for word in paragraph:
    if not word in stopwords:
      new_para.append(word)
  return new_para