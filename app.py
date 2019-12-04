from flask import Flask, request, render_template
from flask_jsonpify import jsonify
import imp
import sys

f, filename, description = imp.find_module('cnn', ['ml-model'])
imp.load_module('cnn', f, filename, description)

# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/robin-api/', methods=['GET'])
def controller():
    print(request.args)
    return jsonify(sys.modules["cnn"].predict(request.args["url"]))

if __name__ == '__main__':

    app.run(port='3000')
