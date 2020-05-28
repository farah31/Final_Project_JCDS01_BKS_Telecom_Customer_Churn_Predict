from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('prediction.html')

@app.route('/profiling')
def insight ():
    return render_template('profiling.html')

@app.route('/insight')
def insight ():
    return render_template('insightplot.html')

# @app.route('/storage/<path:x>')
# def storage(x):
#     return send_from_directory("storage", x)

@app.route('/result', methods=['POST', 'GET'])
def result ():
    if request.method == 'POST':
        input = request.form
        #Gender
        gender = input["gender"]
        strGender = ""
        if gender == "m":
            mal = 1
            fem = 0
            strGender = "Male"
        if gender == "f":
            mal = 0
            fem = 1
            strGender = "Female"
        #SeniorCitizen
        SeniorCitizen = input['SeniorCitizen']
        strSC = ''
        sc = int()
        if SeniorCitizen == 'y':
            sc = 1
            strSC = 'Yes'
        else:
            sc = 0
            strSC = 'No'
        #Partner
        Partner = input['Partner']
        strprt = ''
        prt = int()
        if Partner == 'y':
            prt = 1
            strprt = 'Yes'
        else:
            prt = 0
            strprt = 'No'
        #like
        like = input['like']
        strLike = ''
        lk = int()
        if like == 'y':
            lk = 1
            strLike = 'Yes'
        else:
            lk = 0
            strLike = 'No'
        #hour
        hour = int(input['hour'])
        #Age
        age = int(input['age'])
        #numscreens
        nmsc = int(input['numscreens'])

        # screens
        # screens = input['screens']




        datainput = [[day,hour,age,nmsc,mg,feat,lk]]
        pred = coba.predict(datainput)[0]
        proba = coba.predict_proba(datainput)[0]
        if pred == 0:
            prbb = round((proba[0]*100), 1)
            rslt = "Not Subscribe"
            color = "tomato"
        else:
            prbb = round((proba[1]*100), 1)
            rslt = "Subscribe"
            color = "mediumaquamarine"
        
        # return render_template('result.html')
        return render_template(
            'result.html', dayofweek=strDay, hour=hour, age=age, numscreens=nmsc, minigame=strGame, used_premium_feat=strFeat, 
            like=strLike,result= rslt, proba = prbb, color = color)


if __name__ == '__main__':
    model = joblib.load('model')
    scaler = joblib.load('scalermodel')
    
    app.run(debug=True, port=4400)