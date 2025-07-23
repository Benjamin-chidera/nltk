import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize



text = "This is sentence one. Here is sentence two."
sentences = sent_tokenize(text)  # <-- no language argument needed for English
print(sentences)


text = "Her cat's name is Whiskers."

words = word_tokenize(text)
print(words)