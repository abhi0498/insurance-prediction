import joblib
import pandas as pd

clf = joblib.load('data.pkl')


def predict(age, sex, bmi, children, smoker, region):
    data = dict(
        age=age,

        bmi=bmi,
        sex=sex,
        children=children,
        smoker=smoker,
        region=region)
    dff = pd.DataFrame(data, index=[0])
    dmap = {'male': 0, 'female': 1}
    dff['sex'] = dff['sex'].map(dmap)

    dmap = {'northwest': 0, 'northeast': 1, 'southwest': 2, 'southeast': 3}
    dff['region'] = dff['region'].map(dmap)

    dmap = {'no': 0, 'yes': 1}
    dff['smoker'] = dff['smoker'].map(dmap)

    y = clf.predict(dff.drop('sex', axis=1))
    print(y)
    print(age, sex, bmi, children, smoker, region)
    return y


# predict(age=44,
#         sex='male',
#         bmi=37.1,
#         children=2,
#         smoker='no',
#         region='southwest')
