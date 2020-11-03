from flask import Flask, request, render_template
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pickle

#initialize the app
app = Flask(__name__)
#load the model
model = pickle.load(open('model.pkl', 'rb'))


#redirect the api to homepage
@app.route('/')
def home():
    return render_template('SFCrime.html')

#redirect api to predict result (arrest or release)
@app.route('/predict', methods=['POST'])
def predict():

    #take user input from dashboard and get a prediction 
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int)]
    prediction = model.predict(final_features)

    def final_result(prediction):
        if prediction == 0:
            jail_time_text = "You've been arrested."
            return jail_time_text
        else: 
            no_jail_time_text = "It's your lucky day."
            return no_jail_time_text
        
        

    return render_template('SFCrime.html', prediction_text = final_result )
