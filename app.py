from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename


# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

if __name__ == '__main__':

    app.run()
