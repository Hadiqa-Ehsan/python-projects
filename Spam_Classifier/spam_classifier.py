from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
messages = [
    "Win a free iPhone now",
    "Congratulations you won a lottery",
    "Meeting at 5 pm",
    "Let's have lunch tomorrow",
    "Claim your free prize now",
    "Project deadline is tomorrow"
]

labels = [
    "spam",
    "spam",
    "ham",
    "ham",
    "spam",
    "ham"
]



vectorizer = CountVectorizer()

X = vectorizer.fit_transform(messages)



model = MultinomialNB()

model.fit(X, labels)

new_message = ["Free lottery prize"]

new_X = vectorizer.transform(new_message)

prediction = model.predict(new_X)

print("Prediction:", prediction[0])