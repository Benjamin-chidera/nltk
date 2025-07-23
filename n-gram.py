import nltk
import pandas as pd
import matplotlib.pyplot as plt

token = [
    "machine", "learning", "data", "science", "python", "model",
    "token", "natural", "language", "processing", "algorithm", "training", "to", "the", "apple", "book", "car", "coffee", "door", "friend", "garden",
    "house", "ice", "jacket", "keys", "lamp", "milk", "notebook",
    "orange", "phone", "quiet", "rain", "shoes", "table", "umbrella",
    "vacuum", "window", "xylophone", "yogurt", "zebra", "the", "to"
]

# Flatten the unigram from tuple to string
unigram = pd.Series([w[0] for w in nltk.ngrams(token, 1)]).value_counts(normalize=True)

# Plot top 10 most frequent words
unigram[:10].sort_values().plot.barh(
    color='skyblue', 
    figsize=(12, 8),
    width=0.6
)

plt.title("Top 10 Unigram Frequency Distribution", fontsize=14)
plt.xlabel("Proportion", fontsize=12)
plt.ylabel("Unigrams", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
