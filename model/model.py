# import dependencies
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle
import boto3
import os
import config as cfg
from config import db_user, db_password, db_name, endpoint
from sqlalchemy import create_engine
import psycopg2

# connection
db_string = f"postgres://{db_user}:{db_password}@{endpoint}:5432/{db_name}"
engine = create_engine(db_string)

# load data
print(f"Importing data...\n")
df = pd.read_sql_table(table_name="encoded_data",con=engine)
df = df.drop(columns='Descriptions')
df = df.drop(columns='Months')


# create features
X = df.drop("Resolutions", axis=1)

# create target
y = df["Resolutions"]

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=2020, test_size=0.5)

# train the model
print(f"Training machine learning model...\n")
brf = BalancedRandomForestClassifier()
brf.fit(X_train, y_train)
y_pred = brf.predict(X_test)

# save model via pickle
print(f"Saving model to pickle file...\n")
pickle.dump(brf, open('model.pkl', 'wb'))


# upload our pickle file to s3 so it can be read by dashboard app
if os.path.exists("model.pkl"):

    s3 = boto3.resource('s3',
                        aws_access_key_id=cfg.awsCreds["keyID"],
                        aws_secret_access_key=cfg.awsCreds["secretKey"]
                        )

    try:
        print(f"Uploading pickle file to s3...\n")
        response = s3.meta.client.upload_file(
            'model.pkl', 'group4ds-bucket', 'model.pkl')
        # delete the file after uploading
        print("Upload successful, deleting local pickle file...")
        os.remove("model.pkl")
    except Exception as e:
        print(f"Unable to upload file ", e)
else:
    print(f"Pickle file does not exist, unable to upload to s3\n")
