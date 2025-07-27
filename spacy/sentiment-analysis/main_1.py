from textblob import TextBlob

sentence_1 = "I enjoyed watching the movie."
sentence_2 = "The movie was not good."
sentence_3 = "I hate the weather today."
sentence_4 = "The weather is beautiful today."
sentence_5 = "I enjoyed the movie but the acting was terrible."

print(sentence_1)

sentence_1_sentiment = TextBlob(sentence_1)

print(sentence_1_sentiment.sentiment.polarity)


sentence_2_sentiment = TextBlob(sentence_2)

print(sentence_2_sentiment.sentiment.polarity)