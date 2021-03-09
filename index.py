from flask import Flask,abort, redirect, url_for
from flask import request
from flask import render_template
import os
import json
from os.path import join, dirname
import requests
import io
app = Flask(__name__, static_url_path='/static')
port = int(os.getenv('PORT', 8000))

#Routes

@app.route("/", methods=['POST', 'GET'])
def index():
        return render_template("index.html")


@app.route("/result",methods=['POST','GET'])
def resultpage():
    if request.method == "POST":
        #CALL API

        

        # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
        API_KEY = ""
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields":  ["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

        response_scoring = requests.post('', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        print(response_scoring.json())







        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
