from flask import Flask,jsonify
app = Flask(__name__)
import pandas as pd
import json 

@app.route('/data')
def get_data():
    df = pd.read_excel('names.xlsx')
    df = df[['Full Name','Phone number (WhatsApp Only)']]
    result = df.to_json(orient="split")
    return result