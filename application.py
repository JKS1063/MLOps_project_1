from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__) # initializing a flask app

app = application

# Route for Home Page

@app.route('/') # decorator used to tell the application which URL should call the associated function
def index():
   return render_template('index.html') # rendering the html template 

@app.route('/', methods = ['GET', 'POST']) # predict data route 
def predict_datapoint():
    if request.method == 'GET': # if the request is GET then render the home page
        return render_template('home.html') # rendering the home page
    else:
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))

        ) # getting the data from the user

        pred_df = data.get_data_as_data_frame() # converting the data into data frame
        print(pred_df)

        predict_pipeline = PredictPipeline() # initializing the prediction pipeline
        results = predict_pipeline.predict(pred_df) # predicting the data
        return render_template('home.html', results = results[0]) 
        # rendering the home page with the results, '0' is used because there is only one result and we want to render it as a string

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
