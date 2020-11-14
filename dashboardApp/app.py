
import flask
from flask import render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
import urllib.request
import re
import json

# with urllib.request.urlopen('https://group4ds-bucket.s3.amazonaws.com/model.pkl') as response:
#     pickle = response.read()

# url = 'https://group4ds-bucket.s3.amazonaws.com/model.pkl'
# urllib.request.urlretrieve(url, 'model.pkl')
model = pickle.load(open('model.pkl', 'rb'))
df = pd.read_csv('./Resources/encoded_df.csv')

# initialize the app
app = flask.Flask(__name__)
# load the model
model = pickle.load(
    open('model.pkl', 'rb'))


# redirect the api to homepage
@app.route('/', methods=['GET'])
def main():
    #if flask.request.method == 'GET':
        return render_template('index2.html')


        
@app.route('/formpost', methods=['POST'])
def formpost():
    # create dictionaries of encoded data
        day = {'0': 'Friday', '1': 'Monday', '5': 'Tuesday',
               '2': 'Saturday', '4': 'Thursday', '3': 'Sunday', '6': 'Wednesday'}
        time = {'2': 'Morning', '0': 'Afternoon', '1': 'Evening', '3': 'Night'}
        pddistrict = {'7': 'SOUTHERN', '0': 'BAYVIEW', '9': 'TENDERLOIN', '3': 'MISSION',
                      '4': 'NORTHERN', '8': 'TARAVAL', '2': 'INGLESIDE', '1': 'CENTRAL', '6': 'RICHMOND', '5': 'PARK'}
        month = {'4': 'Jan', '0': 'Apr', '11': 'Sep', '1': 'Aug', '10': 'Oct',
                 '5': 'Jul', '7': 'Mar', '2': 'Dec', '8': 'May', '6': 'Jun', '9': 'Nov'}

        category = {'16': 'WEAPON LAWS', '15': 'WARRANTS', '6': 'NON-CRIMINAL', '0': 'ASSAULT', '8': 'OTHER OFFENSES', '5': 'MISSING PERSON', '4': 'LARCENY/THEFT', '1': 'BURGLARY',
                    '7': 'OTHER', '9': 'ROBBERY', '3': 'FRAUD', '2': 'DRUG/NARCOTIC', '14': 'VEHICLE THEFT', '13': 'VANDALISM', '10': 'SECONDARY CODES', '11': 'SUSPICIOUS OCC', '12': 'TRESPASS'}

        #extract user input from webpage
        #data_dict['Weekdays']
        day_of_week = flask.request.form['Weekdays']
        time_of_day = flask.request.form['ToD']
        police_district = flask.request.form['District']
        crime_category = flask.request.form['Category']
        zip_code = flask.request.form['ZipCode']

        warning=""
        if (not re.match("941\\d{2}",zip_code)):
            warning=f"'{zip_code}' doesn't match SFO ZipCode"
            

        available_zips=['94103', '94124', '94108', '94102', '94109', '94158', '94122', '94116', '94112', '94104', '94110', '94132', '94114', '94131', '94134', '94117', '94115', '94105', '94127', '94118', '94111', '94123', '94107', '94130', '94129']
        
        if zip_code in available_zips:

            #create dataframe for model
            input_variables = pd.DataFrame([[day_of_week, time_of_day, police_district, crime_category, zip_code]], columns=['Dow', 'Tod', 'district', 'category', 'zip'], dtype=str, index=['index'])

            #get models prediction
            prediction = model.predict(input_variables)

            print(prediction)
                
                
            if prediction == 1:
                outcome = "You've committed a crime and gotten away"
            else:
                outcome = "You've most likely been arrested"
        
        else:
            
            outcome = "No available data for introduced ZipCode."

        # Print out final result
        return render_template('index2.html',
        warning=warning, 
        original_input={'Day of Week': day.get(day_of_week), 
                        'Time of Day': time.get(time_of_day), 
                        'Police District': pddistrict.get(police_district), 
                        'Crime Category': category.get(crime_category),
                        'Zip Code': zip_code}, 
        result = outcome )  
        


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0")







        # print(data)
        # data_dict = json.loads(data)
        

        # #get values for ml prediction from data_dict
        # day_of_week = data_dict['day_of_week']
        # time_of_day = data_dict['time_of_day']
        # police_district = data_dict['police_district']
        # crime_category = data_dict['crime_category']
        # zip_code = data_dict['zip_code']

        # day = {'0': 'Friday', '1': 'Monday', '5': 'Tuesday','2': 'Saturday', '4': 'Thursday', '3': 'Sunday', '6': 'Wednesday'}
        # time = {'2': 'Morning', '0': 'Afternoon', '1': 'Evening', '3': 'Night'}
        # pddistrict = {'7': 'SOUTHERN', '0': 'BAYVIEW', '9': 'TENDERLOIN', '3': 'MISSION',
        #               '4': 'NORTHERN', '8': 'TARAVAL', '2': 'INGLESIDE', '1': 'CENTRAL', '6': 'RICHMOND', '5': 'PARK'}

        # category = {'16': 'WEAPON LAWS', '15': 'WARRANTS', '6': 'NON-CRIMINAL', '0': 'ASSAULT', '8': 'OTHER OFFENSES', '5': 'MISSING PERSON', '4': 'LARCENY/THEFT', '1': 'BURGLARY',
        #             '7': 'OTHER', '9': 'ROBBERY', '3': 'FRAUD', '2': 'DRUG/NARCOTIC', '14': 'VEHICLE THEFT', '13': 'VANDALISM', '10': 'SECONDARY CODES', '11': 'SUSPICIOUS OCC', '12': 'TRESPASS'}

        # available_zips=['94103', '94124', '94108', '94102', '94109', '94158', '94122', '94116', '94112', '94104', '94110', '94132', '94114', '94131', '94134', '94117', '94115', '94105', '94127', '94118', '94111', '94123', '94107', '94130', '94129']


        # if zip_code in available_zips:

        #     #create dataframe for model
        #     input_variables = pd.DataFrame([[day_of_week, time_of_day, police_district, crime_category, zip_code]], columns=['Dow', 'Tod', 'district', 'category', 'zip'], dtype=int)

        #     #get models prediction
        #     prediction = model.predict(input_variables)

        #     print(prediction)
                
                
        #     if prediction == 1:
        #         outcome = "You've committed a crime and gotten away"
        #     else:
        #         outcome = "You've most likely been arrested"
        
        # else:
            
        #     outcome = "No available data for introduced ZipCode."
        
        # results_dict = {'prediction':prediction, 'outcome':outcome, 'Day of Week': day.get(day_of_week), 'Time of Day': time.get(time_of_day), 'Police District': pddistrict.get(police_district),
        #                  'Crime Category': category.get(crime_category), 'Zip Code': zip_code}

        # #return JSON results dictionary
        # return jsonify(results_dict)