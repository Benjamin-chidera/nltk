from nltk.stem import PorterStemmer

ps = PorterStemmer()

connect_tokens = ["connecting", "connected", "connectivity", "connects", "connection"]

for t in connect_tokens:
    print(t, ": ", ps.stem(t))