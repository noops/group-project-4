import flask
from flask import render_template
from sklearn.preprocessing import OneHotEncoder
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
        dummy_df = pd.get_dummies(input_variables)
        #get models prediction
        prediction = model.predict(dummy_df)[0]
    
        def final_result(prediction):
            if prediction == 0:
                jail_time_text = "You've been arrested."
                return jail_time_text
            else: 
                no_jail_time_text = "It's your lucky day."
                return no_jail_time_text
            
            

        return render_template('index.html', prediction_text = final_result )



    

if __name__ == "__main__":
    app.run(debug=True)
