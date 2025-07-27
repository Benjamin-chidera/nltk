import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download resources if not already present
nltk.download('punkt')  # for tokenizing text
# nltk.download('averaged_perceptron_tagger')  # for POS tagging

# Sample sentence
example_text = "Wow! The quick brown fox jumps over the lazy dog while the kids laugh happily in the sunlight."

# Tokenize and tag
word_token = word_tokenize(example_text)
print(pos_tag(word_token, lang='eng'))
