from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from PaaS Lab! Student: ARDHRA M P,Reg no: 24MID0086'
