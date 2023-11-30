import json
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib

# load the data from the file
with open('output-miraloma-five.txt', 'r') as file:
    raw_data = json.load(file)

# assume that each item in raw_data is a string representing a dictionary
data = []
for d in raw_data:
    try:
        if d:  # Check if string is not empty
            data.append(json.loads(d))
    except json.JSONDecodeError:
        print(f"Couldn't decode data: {d}")

# remove any entries where 'content' is None or empty
data = [d for d in data if d.get('content')]

# convert the data into two lists: one for the text and one for the labels
texts = [d['content'] for d in data]
labels = [d['site'] for d in data]

# check if there is any data to split
if len(texts) == 0 or len(labels) == 0:
    print("No data to process. Check your data source.")
    exit(1)

# split the data into training and testing sets
texts_train, texts_test, labels_train, labels_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# create a pipeline that vectorizes the text, computes tf-idf scores, and fits a Naive Bayes classifier
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

# fit the pipeline to the training data
text_clf.fit(texts_train, labels_train)

# predict the test set results
predicted = text_clf.predict(texts_test)

# print accuracy, precision, recall and f1_score
print(metrics.classification_report(labels_test, predicted))

# save the model for future use
joblib.dump(text_clf, 'text_clf_model.pkl')