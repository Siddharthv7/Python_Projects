import pickle
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Load pre-trained model & vectorizer
with open("spam_model.pkl", "rb") as model_file:
    clf = pickle.load(model_file)

with open("count_vectorizer.pkl", "rb") as vectorizer_file:
    cv = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    return render_template('index.html', prediction=my_prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
