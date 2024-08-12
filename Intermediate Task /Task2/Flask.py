from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file)
    # Perform analysis (e.g., descriptive stats)
    analysis = data.describe()
    return render_template('analysis.html', tables=[analysis.to_html(classes='data')], titles=data.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
