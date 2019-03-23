from flask import Flask
import os
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    os.system('../client.py 127.0.0.1 65432 3')
    return "Ok"
