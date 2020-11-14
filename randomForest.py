from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced
from sklearn.decomposition import PCA
import pickle
import pandas as pd 

#load data
df = pd.read_csv('/Users/bkirton/Desktop/sanFranCrimePredictor/Resources/encoded_df.csv')
#create features
X = df.drop("Resolutions", axis=1)

#create target
y = df["Resolutions"]

#initialize PCA model 
#use PCA to reduce number of features from 7 to 5 while still capturing most of the variance
pca = PCA(n_components=5)

crime_pca = pca.fit_transform(X)

df = pd.DataFrame(data = crime_pca)
df['Resolutions'] = y

#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2020, test_size=0.5)


# hypertuned parameters 
# {'n_estimators': 200,
#  'min_samples_split': 10,
#  'min_samples_leaf': 2,
#  'max_features': 'sqrt',
#  'max_depth': 50,
#  'bootstrap': True}



#train the model
brf = BalancedRandomForestClassifier(n_estimators=200, min_samples_split=10, min_samples_leaf=2, max_features='sqrt', max_depth=50, bootstrap=True, random_state=2020)
brf.fit(X_train, y_train)
y_pred = brf.predict(X_test)


# Calculated the balanced accuracy score
# balanced_acc_score = balanced_accuracy_score(y_test,y_pred)
# print(f"balanced accuracy score = {balanced_acc_score*100:.2f}%")


# Print the imbalanced classification report
# print("imbalanced classification report")
# print(classification_report_imbalanced(y_test,y_pred))

# Display the confusion matrix
# cm = confusion_matrix(y_test, y_pred)
# cm_df = pd.DataFrame(cm, index=["Acutal 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])
# print(cm_df)

#save model into pickle file
pickle.dump(brf, open('model_2.pkl', 'wb'))
 

