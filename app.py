from flask import Flask, request, render_template
from flask_jsonpify import jsonify
from ml_model import cnn
import sys
import os

# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/robin-api', methods=['POST'])
def controller():
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    file_path = './uploads/img.jpg'
    f.save(file_path)
    return jsonify(cnn.predict(file_path))

if __name__ == '__main__':

    app.run(port='3000')
