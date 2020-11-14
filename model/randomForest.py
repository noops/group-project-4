from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pickle
#import boto3
#import os
#import config as cfg
import pandas as pd 

#load data
df = pd.read_csv('/Users/bkirton/Desktop/sanFranCrimePredictor/Resources/encoded_df.csv')

#create features
X = df.drop("Resolutions", axis=1)

#initialize PCA model 
#use PCA to reduce number of features from 7 to 5 while still capturing most of the variance
pca = PCA(n_components=5)

crime_pca = pca.fit_transform(X)
X = pd.DataFrame(data = crime_pca)
y = df['Resolutions']

#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2020, test_size=0.5)


# hypertuned parameters 
# {'n_estimators': 200,
#  'min_samples_split': 10,
#  'min_samples_leaf': 2,
#  'max_features': 'sqrt',
#  'max_depth': 50,
#  'bootstrap': True}



# train the model
print(f"Training machine learning model...\n")
brf = BalancedRandomForestClassifier(n_estimators=200, min_samples_split=10, min_samples_leaf=2, max_features='sqrt', max_depth=50, bootstrap=True, random_state=2020)
brf.fit(X_train, y_train)
y_pred = brf.predict(X_test)


# save model via pickle
print(f"Saving model to pickle file...\n")
pickle.dump(brf, open('model.pkl', 'wb'))


# # upload our pickle file to s3 so it can be read by dashboard app
# if os.path.exists("model.pkl"):

#     s3 = boto3.resource('s3',
#                         aws_access_key_id=cfg.awsCreds["keyID"],
#                         aws_secret_access_key=cfg.awsCreds["secretKey"]
#                         )

#     try:
#         print(f"Uploading pickle file to s3...\n")
#         response = s3.meta.client.upload_file(
#             'model.pkl', 'group4ds-bucket', 'model.pkl')
#         # delete the file after uploading
#         print("Upload successful, deleting local pickle file...")
#         os.remove("model.pkl")
#     except Exception as e:
#         print(f"Unable to upload file ", e)
# else:
#     print(f"Pickle file does not exist, unable to upload to s3\n")

