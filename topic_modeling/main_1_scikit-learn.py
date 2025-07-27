from main_1_topic_modeling import processed_doc
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


vectorizer = CountVectorizer(max_df=0.95, min_df=2, lowercase=False)

x = vectorizer.fit_transform(processed_doc)

feature_name = vectorizer.get_feature_names_out()

num_of_topics = 3

lda = LatentDirichletAllocation(n_components=num_of_topics, random_state=42)
lda.fit(x)


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-num_of_topics - 1:-1]]
        print(f"Topic {topic_idx + 1}: {', '.join(top_words)}")
        
        
print_top_words(lda, feature_name, 5)