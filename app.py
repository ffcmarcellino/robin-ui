from flask import Flask, request, render_template
from flask_jsonpify import jsonify
import imp
import sys
import os

f, filename, description = imp.find_module('cnn', ['ml-model'])
imp.load_module('cnn', f, filename, description)

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
    return jsonify(sys.modules["cnn"].predict(file_path))

if __name__ == '__main__':

    app.run(port='3000')
