import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

text = "I am going to the store because I need some milk."

filter_words = [word for word in word_tokenize(text) if word.lower() not in stop_words]

# print("Stop words:", stop_words)

print("Original text:", text)
print("Filtered text:", filter_words)