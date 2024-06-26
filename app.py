# Importing packages
from src.components.create_custom_data import CustomData
from src.pipelines.predict_pipeline import PredictPipeline
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

# Instantiating the Flask application
app = Flask(__name__)

# Defining the home page
@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

# Creating the predict datapoint function
@app.route('/predict.html', methods=['GET', 'POST'])
def predict_datapoint():
    # Displaying the home page if the method is GET
    # else run the prediction
    if request.method == 'GET':
        return render_template('predict.html') 
    else:
        data = CustomData(
            V1 = float(request.form.get('V1')),
            V2 = float(request.form.get('V2')),
            V3 = float(request.form.get('V3')),
            V4 = float(request.form.get('V4')),
            V5 = float(request.form.get('V5')),
            V6 = float(request.form.get('V6')),
            V7 = float(request.form.get('V7')),
            V8 = float(request.form.get('V8')),
            V9 = float(request.form.get('V9')),
            V10 = float(request.form.get('V10')),
            V11 = float(request.form.get('V11')),
            V12 = float(request.form.get('V12')),
            V13 = float(request.form.get('V13')),
            V14 = float(request.form.get('V14')),
            V15 = float(request.form.get('V15')),
            V16 = float(request.form.get('V16')),
            V17 = float(request.form.get('V17')),
            V18 = float(request.form.get('V18')),
            V19 = float(request.form.get('V19')),
            V20 = float(request.form.get('V20')),
            V21 = float(request.form.get('V21')),
            V22 = float(request.form.get('V22')),
            V23 = float(request.form.get('V23')),
            V24 = float(request.form.get('V24')),
            V25 = float(request.form.get('V25')),
            V26 = float(request.form.get('V26')),
            V27 = float(request.form.get('V27')),
            V28 = float(request.form.get('V28')),
            Amount = float(request.form.get('Amount'))
        )
        
        # Creating a dataframe from the custom data
        df = data.get_data_as_dataframe()
        
        # Instantiating the prediction pipeline and predicting
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(df)
        return render_template('predict.html', results=pred, pred_df=df)
    

# Creating a function to define an api call
@app.route('/predictAPI', methods=['POST'])
@cross_origin()
def predict_api():
    if request.method == 'POST':
         data = CustomData(
            V1 = float(request.form.get('V1')),
            V2 = float(request.form.get('V2')),
            V3 = float(request.form.get('V3')),
            V4 = float(request.form.get('V4')),
            V5 = float(request.form.get('V5')),
            V6 = float(request.form.get('V6')),
            V7 = float(request.form.get('V7')),
            V8 = float(request.form.get('V8')),
            V9 = float(request.form.get('V9')),
            V10 = float(request.form.get('V10')),
            V11 = float(request.form.get('V11')),
            V12 = float(request.form.get('V12')),
            V13 = float(request.form.get('V13')),
            V14 = float(request.form.get('V14')),
            V15 = float(request.form.get('V15')),
            V16 = float(request.form.get('V16')),
            V17 = float(request.form.get('V17')),
            V18 = float(request.form.get('V18')),
            V19 = float(request.form.get('V19')),
            V20 = float(request.form.get('V20')),
            V21 = float(request.form.get('V21')),
            V22 = float(request.form.get('V22')),
            V23 = float(request.form.get('V23')),
            V24 = float(request.form.get('V24')),
            V25 = float(request.form.get('V25')),
            V26 = float(request.form.get('V26')),
            V27 = float(request.form.get('V27')),
            V28 = float(request.form.get('V28')),
            Amount = float(request.form.get('Amount'))
        )
         
         # Creating a dataframe from the custom data
         df = data.get_data_as_dataframe()
         
         # Instantiating the prediction pipeline and predicting
         predict_pipeline = PredictPipeline()
         pred = predict_pipeline.predict(df)
         
         # Creating a dictionary
         dct = {'Prediction': pred}
         
         return jsonify(dct)


# Running the script
if __name__ == '__main__':
    app.run(debug=True)

        
        