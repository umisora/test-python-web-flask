from flask import request, jsonify
from main import app


@app.route('/')
def show_entries():
    return 'Hello, World!'


@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello, world'})
