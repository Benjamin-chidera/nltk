import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

connect_tokens = ["connecting", "connected", "connectivity", "connects", "connection"]


for t in connect_tokens:
    print(t, ": ", lemmatizer.lemmatize(t))