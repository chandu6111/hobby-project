import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('linear_regression_model_sc.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/predict_now.html')
def page_predict():
    return render_template('predict_now.html')


@app.route('/predict', methods=['GET', 'post'])
def predict():
    GRE_Score = int(request.form['GRE Score'])
    TOEFL_Score = int(request.form['TOEFL Score'])
    University_Rating = int(request.form['University Rating'])
    SOP = float(request.form['SOP'])
    LOR = float(request.form['LOR'])
    CGPA = float(request.form['CGPA'])
    Research = int(request.form['Research'])

    final_features = pd.DataFrame(
        [[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])

    predict = model.predict(final_features)

    output = predict[0]

    return render_template('predict_now.html', prediction_text='Admission chances are {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)


'''
def predict():
    if request.method=='POST':
        features=[str(x) for x in request.form.values()]
        gre=int(features[0])
        toefl=int(features[1])
        ur=float(features[2])
        sop=float(features[3])
        lor=float(features[4])
        cgpa=float(features[5])
        research=int(features[6])
        final_features=[]
        final_features.append(gre)
        final_features.append(toefl)
        final_features.append(ur)
        final_features.append(sop)
        final_features.append(lor)
        final_features.append(cgpa)
        final_features.append(research)
        lr_model=pickle.load(open("model.pkl","rb"))

        prediction=lr_model.predict([final_features])
        output=round(prediction[0],2)
        output=output*100;
    return render_template('out.html',prediction_text=output)


    prediction_text=Admission chances are {}.format(output)

'''
