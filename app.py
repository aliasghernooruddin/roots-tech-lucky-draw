from flask import Flask, jsonify, request
import pandas as pd
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS

cred = credentials.Certificate("./firebase-credentials.json")

FIRESTORE = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    df = pd.read_excel('names.xlsx')
    df = df[['Full Name', 'Contact Number (WhatsApp Only)', 'Mohallah']]
    df = df.fillna(0)
    result = df.to_dict(orient="split")

    df2 = pd.read_excel('gifts.xlsx')
    result2 = df2['Gifts'].tolist()
    data = {'names': result, 'gifts': result2}
    
    return jsonify(data)


@app.route('/update', methods=['POST'])
def update_data():
    try:
        data = json.loads(request.data)
        doc_ref = db.collection(u'winners').document()
        doc_ref.set(data)
        return jsonify({'data': True})
    except:
        print("error")
        return jsonify({'data': True})


@app.route('/finalList', methods=['POST'])
def final_list():
    data = json.loads(request.data)
    df = pd.DataFrame(data['finalList'])
    df.to_excel('winners.xlsx', index=False)
    return jsonify({'data': True})
