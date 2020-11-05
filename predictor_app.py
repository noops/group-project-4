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
        
        #dictionaries of our encoded values
        pddistrict_dict = {'7': 'Bayview', '0': 'Central', '9': 'Ingleside', '3': 'Mission', '4': 'Park', '8': 'Southern', '2': 'Taraval', '1': 'Tenderlion', '6': 'Richmond', '5': 'Northern'}        
        
        category_dict = {'16': 'Weapon Laws', '15': 'Warrants', '6': 'Non-Criminal', '0': 'Assault', '8': 'Other Offenses', '5': 'Missing Person', '4': 'Larceny/Theft', '1': 'Burglary', 
        '7': 'Other', '9': 'Robbery', '3': 'Fraud', '2': 'Drug/Narcotic', '14': 'Vehicle theft', '13': 'Vandalism', '10': 'Secondary Codes', '11': 'Suspicious Activity', '12': 'Trespass'}
        
        day = {'0': 'Friday', '1': 'Monday', '5': 'Tuesday', '2': 'Saturday', '4': 'Thursday', '3': 'Sunday', '6': 'Wednesday'}
        time = {'2':'Morning', '0':'Afternoon', '3':'Night', '1':'Evening'}
        
        #extract user input from webpage
        dayOfWeek = flask.request.form['days']
        timeOfDay = flask.request.form['time_of_day']
        pddistrict = flask.request.form['District']
        category = flask.request.form['Category']

        

        #create dataframe for model
        input_variables = pd.DataFrame([[dayOfWeek, timeOfDay, pddistrict, category]], columns=['day', 'time_of_day', 'district', 'category'], dtype=str, index=['index'])

       

        #get models prediction
        prediction = model.predict(input_variables)
            
            
        if prediction == 1:
            outcome = "You've committed a crime and gotten away"
        else:
            outcome = "You've most likely been arrested"

        return render_template('index.html', 
        original_input={'Day of Week': day.get(dayOfWeek), 
                        'Time of Day': time.get(timeOfDay), 
                        'Police District': pddistrict_dict.get(pddistrict), 
                        'Crime Category': category_dict.get(category)}, 
        result = outcome )



    

if __name__ == "__main__":
    app.run(debug=True)
