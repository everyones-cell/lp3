import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../input/email-spam-classification-dataset-csv/emails.csv")

df.head(20)

# Check missing values
df.isnull().sum()

# Dataset description
df.describe()

# Correlation
df.corr()

# Separate features and target
X = df.iloc[:, 1:3001]
Y = df.iloc[:, -1].values

# Split dataset
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, test_size=0.25, random_state=42
)

# Feature scaling
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)

# Train model
knn.fit(train_x, train_y)

# Prediction
y_pred = knn.predict(test_x)

# Accuracy
print("Accuracy Score for KNN:", accuracy_score(test_y, y_pred) * 100)
