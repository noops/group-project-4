from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 
import pickle


#load data
df = pd.read_csv('/Users/bkirton/Desktop/sanFranCrimePredictor/Resources/pca_df.csv')

#create features
X = df.drop("Target", axis=1)

#create target
y = df["Target"]

#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.5)

#train the model
brf = BalancedRandomForestClassifier()
brf.fit(X_train, y_train)

#predict test set results

y_pred = brf.predict(X_test)

#save model via pickle
pickle.dump(brf, open('model.pkl', 'wb'))