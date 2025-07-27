import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

examples = ["running", "eating", "doing", "going", "walking", "flying","connecting", "connected", "connectivity", "connects", "connection", "churches"]


lemmatized = [lemmatizer.lemmatize(word) for word in examples]

print(lemmatized)