from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 
import pickle


#load data

df = pd.read_csv('./Resources/encoded_df.csv')
df = df.drop(columns='Descriptions')
df = df.drop(columns='Months')


#create features
X = df.drop("Resolutions", axis=1)

#create target
y = df["Resolutions"]




#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2020, test_size=0.5)


#train the model
brf = BalancedRandomForestClassifier()
brf.fit(X_train, y_train)
y_pred = brf.predict(X_test)



#save model via pickle
pickle.dump(brf, open('model.pkl', 'wb'))