from flask import Flask, redirect, render_template, request

import pandas as pd
from api import predict
app = Flask(__name__)
age = sex = children = smoker = region = bmi = 0


@app.route('/user', methods=['POST', 'GET'])
def user():
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

        return redirect('/results')


@app.route('/results', methods=['GET'])
def result():
    y_p = predict(age=age,
                  sex=sex,
                  bmi=bmi,
                  children=children,
                  smoker=smoker,
                  region=region)

    y_p = f'{y_p[0]:.2f}'

    old = pd.read_csv('new-data.csv')
    print(old)
    f = dict(
        index=len(old),
        age=[age],
        sex=[sex],
        bmi=[bmi],
        children=[children],
        smoker=[smoker],
        region=[region],
        charges=[y_p],
    )
    new_data = pd.DataFrame(f)
    print(new_data)
    df = pd.concat([old, new_data])
    print(df)

    df.to_csv('new-data.csv')
    return render_template('results.html', f=f)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/client/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.form['UserId'] == 'admin' and request.form['Password'] == 'admin': #change this to check in  db
            return render_template('vis.html')
        else:
            return render_template('error.html')


@app.route('/client', methods=['GET', 'POST'])
def client():

    return render_template('vis.html')


@app.route('/algorithm', methods=['GET'])
def algo():
    return render_template('algorithms.html')


@app.route('/descriptive', methods=['GET'])
def desc():
    return render_template('data_des_stat.html')


if(__name__ == '__main__'):
    app.run(debug=True)
