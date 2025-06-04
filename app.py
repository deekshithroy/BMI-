from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bmi_form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            result = "Underweight"
        elif 18.5 <= bmi < 24.9:
            result = "Normal weight"

        elif 25 <= bmi < 29.9:
            result = "Overweight"
        else:
            result = "Obese"

        return render_template('bmi_result.html', bmi=bmi, result=result)

    except Exception as e:
        return f"<h3>Error: {e}</h3>"

if __name__ == '_main_':
    app.run(debug=True)