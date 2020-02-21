
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
import json
from collections import OrderedDict
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask import jsonify
import requests
import urllib.request
import traceback
import uploadFile

app = Flask(__name__, static_url_path='')
CORS(app)
ALLOWED_EXTENSIONS = set(['csv'])

port = int(os.getenv('PORT', 5002))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadCsv', methods=['POST'])
def upload_file():
    try:
        request.files['file']
    except Exception as e:
        traceback.print_exc()
        return str(e)
    else:
        try:
            if not allowed_file(request.files['file'].filename):
                raise ValueError('wrong file extension')
            else:
                uploaded_file = request.files['file']
                uploadFile.import_csvfile(uploaded_file)
                return "successfull"
        except Exception as e:
            traceback.print_exc()
            return str(e)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port, debug=True)
