import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score,classification_report
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

DataSet = pd.DataFrame()
DataSet = pd.read_csv("/kaggle/input/diabetes/diabetes.csv")
DataSet.head(10)

for column in DataSet.columns[1:-3]:
    DataSet[column].replace(0,np.NaN, inplace=True)
    DataSet[column].fillna(round(DataSet[column].mean(skipna=True)), inplace=True)
DataSet.head(10)

X = DataSet.drop("Outcome",axis=1)
y = DataSet["Outcome"]
# Split data into 20% for testing and 80% for training
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

neighbor = KNeighborsClassifier(n_neighbors=5,metric="euclidean")
neighbor.fit(X_train,y_train)

y_pred = neighbor.predict(X_test)
y_pred

print(confusion_matrix(y_pred,y_test))

print(accuracy_score(y_pred,y_test))

print(classification_report(y_pred,y_test))
