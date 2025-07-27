import nltk
nltk.download("punkt")
from nltk.tokenize import word_tokenize, sent_tokenize

text = "The Natural Language Toolkit (NLTK) is a powerful Python library used for working with human language data. It provides tools for tasks like tokenizing strings into words or sentences, removing stopwords, and analyzing text structure. Using nltk, you can process and clean raw strings for use in NLP applications like sentiment analysis, chatbots, or search engines."

word = word_tokenize(text)
print(word) # this will split the text into words

print("-" * 50) # this will print a line of 50 dashes


sentence = sent_tokenize(text)
print(sentence) # this will split the text into sentences