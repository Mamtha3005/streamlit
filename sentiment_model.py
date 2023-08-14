import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Mock dataset
sentences = [
    "I love this product!",
    "It's not bad.",
    "This is terrible.",
]
labels = [2, 1, 0]  # Positive, Neutral, Negative

# Create a pipeline: Text vectorization + Naive Bayes classifier
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Fit the model
pipeline.fit(sentences, labels)

# Save the model as a pickle file
joblib.dump(pipeline, 'sentiment_model.pkl')