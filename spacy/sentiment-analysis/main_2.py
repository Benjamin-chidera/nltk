from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentence_1 = "I enjoyed watching the movie."
sentence_2 = "The movie was not good."
sentence_3 = "I hate the weather today."
sentence_4 = "The weather is beautiful today."
sentence_5 = "I enjoyed the movie but the acting was terrible."

analyzer = SentimentIntensityAnalyzer()

vs = analyzer.polarity_scores(sentence_5)
print(vs)