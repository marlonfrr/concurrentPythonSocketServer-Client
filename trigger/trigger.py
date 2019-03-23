from flask import Flask
from flask import request
import os
import subprocess
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    body = request.data
    os.system('../client.py 127.0.0.1 65432 1 '+str(body, 'utf-8'))
    return "Ok"
