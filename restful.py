from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'welcome to flask zone'})





# activate DEBUG mode
# FLASK_APP=restful.py FLASK_DEBUG=1 python -m flask run