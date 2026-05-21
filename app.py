from flask import Flask, render_template, request, jsonify
import pickle
import re

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Feature extraction (simple simulation)
def extract_features(url):
    length = len(url)
    has_https = 1 if "https" in url else 0
    has_ip = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    has_at = 1 if "@" in url else 0
    return [[length, has_https, has_ip, has_at]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/security')
def security():
    return render_template('security.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"result": "Invalid URL"})

    features = extract_features(url)
    import pandas as pd
    features_df = pd.DataFrame(features, columns=['length', 'https', 'ip', 'at'])
    prediction = model.predict(features_df)[0]

    result = "Safe" if prediction == 0 else "Phishing"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)