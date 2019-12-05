from flask import Flask, request, render_template
from flask_jsonpify import jsonify
import imp
import sys
import os
from werkzeug.utils import secure_filename

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
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
    basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)
    return jsonify(sys.modules["cnn"].predict(file_path))

if __name__ == '__main__':

    app.run(port='3000')
