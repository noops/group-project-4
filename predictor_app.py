import flask
from flask import render_template
import numpy as np
import pandas as pd
import pickle

#initialize the app
app = flask.Flask(__name__)
#load the model
model = pickle.load(open('model.pkl', 'rb'))


#redirect the api to homepage
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('index.html')
    
    if flask.request.method == 'POST':
        #extract user input from webpage
        day_of_week = flask.request.form['Weekdays']
        time_of_day = flask.request.form['ToD']
        police_district = flask.request.form['District']
        crime_category = flask.request.form['Category']


        #create dataframe for model
        input_variables = pd.DataFrame([[day_of_week, time_of_day, police_district, crime_category]], columns=['Dow', 'Tod', 'district', 'category'], dtype=str, index=['index'])
        #get dummy vals for strings
        dummy_df = pd.get_dummies(input_variables)

        
        
        #get missing columns 
        features = model.n_features_
        number_of_columns = len(dummy_df.columns)
        missing_columns = features - number_of_columns
        
        #create new columns filled with zero to reach 50 columns for model to run 
        for column in range(missing_columns):
            dummy_df[column]=0

        #get models prediction
        prediction = model.predict(dummy_df)

        print(prediction)
            
            
        if prediction == 1:
            outcome = "You've committed a crime and gotten away"
        else:
            outcome = "You've most likely been arrested"

        return render_template('index.html', 
        original_input={'Day of Week': day_of_week, 
                        'Time of Day': time_of_day, 
                        'Police District': police_district, 
                        'Crime Category': crime_category}, 
        result = outcome )



    

if __name__ == "__main__":
    app.run(debug=True)
