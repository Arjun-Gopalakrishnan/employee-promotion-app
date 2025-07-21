from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_values = [
            float(request.form['gender']),
            float(request.form['relevant_experience']),
            float(request.form['enrolled_university']),
            float(request.form['education_level']),
            float(request.form['major_discipline']),
            float(request.form['experience']),
            float(request.form['company_size']),
            float(request.form['company_type']),
            float(request.form['last_new_job']),
            float(request.form['training_hours']),
            float(request.form['city_development_index']),
        ]

        prediction = model.predict([input_values])
        result = "Promoted ✅" if prediction[0] == 1 else "Not Promoted ❌"
        return render_template('index.html', prediction_text=result)
    
    except Exception as e:
        return render_template('index.html', prediction_text="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)

