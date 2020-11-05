from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 
import pickle


#load data
df = pd.read_csv('/Users/bkirton/Desktop/sanFranCrimePredictor/Resources/encoded_df.csv')
df = df.drop(columns='Months')
df = df.drop(columns='Descriptions')
df = df.drop(columns='ZipCode')

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


# assign each category, pddistrict, timeOfDay, day to a number. Use this number for predictions in ML model.
# timeOfDay{morning:2, afternoon:0, night:3, evening:1}
# pddistrict {Bayview: 7, Central: 0, Ingleside: 9, Mission: 3, Park: 4, Southern: 8, Taraval: 2, Tenderlion: 1, Richmond: 6, Northern: 5}
# category{weapon laws: 16, warrants: 15, non-criminal: 6, assault: 0, other offenses: 8, missing person: 5, larceny/theft: 4, burglary: 1, other: 7, robbery: 9, fraud: 3, drug/narcotic: 2, vehicle theft: 14, vandalism: 13, secondary codes: 10, suspicious occ: 11, trespass: 12}
# day{friday: 0, monday: 1, tuesday: 5, saturday: 2, thursday: 4, sunday: 3, wednesday: 6}
# array(['Jan', 'Apr', 'Sep', 'Feb', 'Oct', 'Aug', 'Jul', 'Mar', 'Dec', 'May', 'Jun', 'Nov'], dtype=object)
# array([ 4,  0, 11,  3, 10,  1,  5,  7,  2,  8,  6,  9])