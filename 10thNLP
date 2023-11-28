from sklearn.feature_extraction.text import TfidfVectorizer

# Sample Documents
documents = [
    "Natural language processing (NLP) is a field of study in artificial intelligence.",
    "NLP techniques are used in various applications like machine translation and sentiment analysis.",
    "The development of NLP tools and libraries has made text analysis easier."
]

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Calculate TF-IDF scores
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Display TF-IDF scores for each term in each document
terms = tfidf_vectorizer.get_feature_names_out()

for i, doc in enumerate(documents):
    print(f"TF-IDF scores for Document {i+1}:")
    feature_index = tfidf_matrix[i,:].nonzero()[1]
    scores = zip(feature_index, [tfidf_matrix[i, x] for x in feature_index])
    for term, score in [(terms[i], score) for i, score in scores]:
        print(f"  {term}: {score}")
