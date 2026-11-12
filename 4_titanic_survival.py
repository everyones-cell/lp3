import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# train.csv is the Kaggle Titanic training dataset
data = pd.read_csv("train.csv")
data = data[["Pclass", "Sex", "Age", "SibSp", "Parch",
             "Fare", "Embarked", "Survived"]]

data["Age"] = data["Age"].fillna(data["Age"].median())
data["Fare"] = data["Fare"].fillna(data["Fare"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

data["Sex"] = LabelEncoder().fit_transform(data["Sex"])
data["Embarked"] = LabelEncoder().fit_transform(data["Embarked"])

X = data.drop("Survived", axis=1)
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
