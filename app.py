from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('prediction.html')

@app.route('/profiling')
def profiling ():
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
        #Dependents
        Dependents = input['Dependents']
        strdpd = ''
        dpd = int()
        if Dependents == 'y':
            dpd = 1
            strdpd = 'Yes'
        else:
            dpd = 0
            strdpd = 'No'
        #PhoneService
        PhoneService = input['PhoneService']
        strphone = ''
        phone = int()
        if PhoneService == 'y':
            phone = 1
            strphone = 'Yes'
        else:
            phone = 0
            strphone = 'No'
        #MultipleLines
        MultipleLines = input['MultipleLines']
        strml = ''
        ml = int()
        if MultipleLines == 'y':
            ml = 1
            strml = 'Yes'
        elif MultipleLines == 'n':
            ml = 0
            strml = 'No'
        else:
            ml = 0
            strml = 'No phone service'
        #InternetService
        InternetService = input['InternetService']
        strins = ''
        if InternetService == 'dsl':
            dsl = 1
            fo = 0
            n = 0
            strins = 'DSL'
        elif InternetService == 'fo':
            dsl = 0
            fo = 1
            n = 0
            strins = 'FiberOptic'
        else:
            dsl = 0
            fo = 0
            n = 1
            strins = 'NoIntServ'
        #OnlineSercurity
        OnlineSecurity = input['OnlineSecurity']
        stros = ''
        os = int()
        if OnlineSecurity == 'y':
            os = 1
            stros = 'Yes'
        else:
            os = 0
            stros = 'No'
        #OnlineBackup
        OnlineBackup = input['OnlineBackup']
        strob = ''
        ob = int()
        if OnlineBackup == 'y':
            ob = 1
            strob = 'Yes'
        else:
            ob = 0
            strob = 'No'
        #DeviceProtection
        DeviceProtection = input['DeviceProtection']
        strdp = ''
        dp = int()
        if DeviceProtection == 'y':
            dp = 1
            strdp = 'Yes'
        else:
            dp = 0
            strdp = 'No'
        #TechSupport
        TechSupport = input['TechSupport']
        strts = ''
        ts = int()
        if TechSupport == 'y':
            ts = 1
            strts = 'Yes'
        else:
            ts = 0
            strts = 'No'
        #StreamingTV
        StreamingTV = input['StreamingTV']
        strtv = ''
        tv = int()
        if StreamingTV == 'y':
            tv = 1
            strtv = 'Yes'
        else:
            tv = 0
            strtv = 'No'
        #StreamingMovies
        StreamingMovies = input['StreamingMovies']
        strmv = ''
        mv = int()
        if StreamingMovies == 'y':
            mv = 1
            strmv = 'Yes'
        else:
            mv = 0
            strmv = 'No'
        #Contract
        Contract = input['Contract']
        strcon = ''
        if Contract == 'mtm':
            mtm = 1
            one = 0
            two = 0
            strcon = 'Month-to-month'
        elif Contract == 'one':
            mtm = 0
            one = 1
            two = 0
            strcon = 'One year'
        else:
            mtm = 0
            one = 0
            two = 1
            strcon = 'Two year'
        #PaperlessBilling
        PaperlessBilling = input['PaperlessBilling']
        strpb = ''
        pb = int()
        if PaperlessBilling == 'y':
            pb = 1
            strpb = 'Yes'
        else:
            pb = 0
            strpb = 'No'
        #PaymentMethod
        PaymentMethod = input['PaymentMethod']
        strpm = ''
        if PaymentMethod == 'bt':
            bt = 1
            cc = 0
            ec = 0
            mc = 0
            strpm = 'Bank transer (automatic)'
        elif PaymentMethod == 'cc':
            bt = 0
            cc = 1
            ec = 0
            mc = 0
            strpm = 'Credit card (automatic)'
        elif PaymentMethod == 'ec':
            bt = 0
            cc = 0
            ec = 1
            mc = 0
            strpm = 'Electronic check'
        else:
            bt = 0
            cc = 0
            ec = 0
            mc = 1
            strpm = 'Mailed check'
        #tenure
        tenure = float(input['tenure'])
        #MonthlyCharges
        MonthlyCharges = float(input['MonthlyCharges'])
        #TotalCharges
        TotalCharges = float(input['TotalCharges'])

        
        #Result
        datainput = [[fem, mal, dsl, fo, n, mtm, one, two, bt, cc, ec, mc, sc, prt, dpd, tenure, phone, ml, os, ob, dp, ts, tv, mv, pb, MonthlyCharges, TotalCharges]]
        scaled = scaler.transform(datainput)
        pred = modelfix.predict(scaled)[0]
        proba = modelfix.predict_proba(scaled)[0]
        if pred == 0:
            prbb = round((proba[0]*100), 1)
            rslt = "RETAIN"
            color = "tomato"
        else:
            prbb = round((proba[1]*100), 1)
            rslt = "EXIT"
            color = "mediumaquamarine"
        
        # return render_template('result.html')
        return render_template(
            'result.html', gender=strGender, InternetService=strins, Contract=strcon, PaymentMethod=strpm, SeniorCitizen=strSC, Partner=strprt, 
            Dependents=strdpd, tenure=tenure, PhoneService=strphone, MultipleLines=strml, OnlineSecurity=stros, OnlineBackup=strob, DeviceProtection=strdp, TechSupport=strts,
            StreamingTV=strtv, StreamingMovies=strmv, PaperlessBilling=strpb, MonthlyCharges=MonthlyCharges, TotalCharges=TotalCharges, result= rslt, proba = prbb, color = color)


if __name__ == "__main__":
    modelfix = joblib.load("modelfix")
    scaler = joblib.load("scalermodel")
    
    app.run(debug=True, port=4400)