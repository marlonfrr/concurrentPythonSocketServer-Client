from flask import Flask
from flask import request
from flask import jsonify
import os
import subprocess
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    body = request.data
    # os.system('../client.py 127.0.0.1 65432 1 '+str(body, 'utf-8'))
    getVersion =  subprocess.Popen(["python3", "../client.py", "127.0.0.1", "65432", "1" ,str(body, 'utf-8')], stdout=subprocess.PIPE).stdout
    version =  getVersion.read()
    result = "error"
    if "successful" in str(version):
        result = "Conectado correctamente"
        print("Bien")
    else:
        result = "Error al autenticar"
        print("Mal")
    return jsonify(result)
