from flask import Flask,abort, redirect, url_for
from flask import request
from flask import render_template
import os
import json
from os.path import join, dirname
import requests
import io
import time


app = Flask(__name__)
port = int(os.getenv('PORT', 8000))

#Routes

@app.route("/", methods=['POST', 'GET'])
def index():
        return render_template("index.html")


@app.route("/resultpage",methods=['POST','GET'])
def resultpage():
    if request.method == "POST":
        #CALL API
        
        fixed_acidity=request.form["fixed acidity"]
        #print(int(fixed_acidity))
        volatile_acidity=request.form["volatile acidity"]
        

        citric_acid=request.form["citric acid"]


        residual_sugar=request.form["residual sugar"]


        chlorides=request.form["chlorides"]


        free_sulfur_dioxide=request.form["free sulfur dioxide"]


        total_sulfur_dioxide=request.form["total sulfur dioxide"]


        density=request.form["density"]


        pH=request.form["pH"]

        print("ph",pH)
        sulphates=request.form["sulphates"]


        alcohol=request.form["alcohol"]
        
        print("post called")

        # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
        API_KEY = ""
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {
        "input_data": [
        {
        "fields": [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol"
        ],
        "values": [[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol
        ]]
    }
  ]
}

        response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/488fec18-46b8-413b-9993-db97e1614edf/predictions?version=2021-03-08', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        print(response_scoring.json())

        result=response_scoring.json()["predictions"][0]["values"][0][0]
        print(str(result))
        y=str(result)
        time.sleep(3)
        
        print("here")
        return (y)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
