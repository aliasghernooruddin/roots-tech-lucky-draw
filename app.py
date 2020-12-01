from flask import Flask,jsonify, request
import pandas as pd
import json 
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./firebase-credentials.json")

FIRESTORE = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    df = pd.read_excel('names.xlsx')
    df = df[['Full Name','Phone number (WhatsApp Only)']]
    result = df.to_json(orient="split")
    return result


@app.route('/update', methods=['POST'])
def update_data():
    data = json.loads(request.data)
    doc_ref = db.collection(u'winners').document()
    doc_ref.set(data)
    return jsonify({'data':True})