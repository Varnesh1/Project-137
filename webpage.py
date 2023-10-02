from flask import Flask, jsonify, request
from data import data

app = Flask(__name__) 

@app.route("/")
def data1234():
    return jsonify({
        'data' : data,
        'message' : 'success'
        
    })