from flask import Flask, redirect, render_template, request

import pandas as pd
from api import predict
app = Flask(__name__)
age = sex = children = smoker = region = bmi = 0


@app.route('/', methods=['POST', 'GET'])
def home():
    global age, sex, children, smoker, region, bmi
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form['sex']
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']
        bmi = float(request.form['bmi'])
        print(type(children))
        return redirect('/results')


@app.route('/results', methods=['GET'])
def result():
    y_p = predict(age=age,
                  sex=sex,
                  bmi=bmi,
                  children=children,
                  smoker=smoker,
                  region=region)
    f = dict(
        y=y_p,
        age=age,
        sex=sex,
        bmi=bmi,
        children=children,
        smoker=smoker,
        region=region
    )
    return render_template('results.html', f=f)


if(__name__ == '__main__'):
    app.run(debug=True)
