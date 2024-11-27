from summ import summarize
from flask import Flask, request, render_template, jsonify, make_response
from time import sleep
from flask_cors import CORS
from config.db import get_connection
# import os
# import signal



app = Flask(__name__)
CORS(app)
db = get_connection()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/getSummary", methods=["POST"])
def getSummary():
    data = request.get_json()
    query = data['query']
    response = summarize(query)
    response_object = make_response(jsonify({"response": response}))
    response_object.status_code = 200

    return response_object

@app.route("/getTransactions", methods=["GET"])
def get_transactions():
    docs = list(db['transactions'].find())
    response_object = make_response(jsonify({"response" : docs}))
    response_object.status_code = 200
    response_object.mimetype = "application/json"
    return response_object





if __name__ == "__main__":
    app.run(debug=True)