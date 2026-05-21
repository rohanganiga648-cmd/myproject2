import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv('dataset.ipynb')

X = data[['length', 'https', 'ip', 'at']]
y = data['label']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved as model.pkl")