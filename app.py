from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['crim']),
        float(request.form['zn']),
        float(request.form['indus']),
        float(request.form['chas']),
        float(request.form['nox']),
        float(request.form['rm']),
        float(request.form['age']),
        float(request.form['dis']),
        float(request.form['rad']),
        float(request.form['tax']),
        float(request.form['ptratio']),
        float(request.form['b']),
        float(request.form['lstat'])
    ]

    prediction = model.predict([features])

    return render_template(
        'home.html',
        prediction_text=f"Predicted House Price: {prediction[0]:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)