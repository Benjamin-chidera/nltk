from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

examples = ["running", "eating", "doing", "going", "walking", "flying"]

stemmed_words = [stemmer.stem(word) for word in examples]

print(stemmed_words)