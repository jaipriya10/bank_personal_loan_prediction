import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

data = pd.read_csv("Bank_Personal_Loan_Modelling.csv")

data.rename(columns = {'ZIP Code':'ZIP_Code','Personal Loan':'Personal_Loan','Securities Account':'Securities_Account','CD Account':'CD_Account'},inplace = True)

other_features = [ 'Age', 'Experience', 'Income', 'ZIP_Code', 'Family', 'CCAvg','Education', 'Mortgage', 'Securities_Account','CD_Account', 'Online', 'CreditCard']
X = data[other_features]
y = data["Personal_Loan"]


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.30, random_state=10)

model3= RandomForestClassifier(random_state=10, n_jobs=-1, max_depth=5,n_estimators=150, oob_score=True)
model3.fit(X_train, y_train)
y_pred_value = model3.predict(X_test)
accuracy = accuracy_score(y_test, y_pred_value)

import pickle
filename = 'model.pkl'
pickle.dump(model3, open(filename, 'wb'))


