from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name' : 'javascript'}, {'name' : 'python'}, { 'name' : 'ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'welcome to flask zone'})

@app.route('/lang', methods=['GET'])
def all_language():
    return jsonify({'laguages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def one_language(name): 
    return jsonify({"languages" : [lang for lang in languages if lang['name'] == name]})

@app.route('/lang', methods=['POST'])
def add_one():
    language = {'name' : request.json['name']}
    languages.append(language)

    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def edit_one(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']

    return jsonify({'languages' : langs[0]})

if __name__ == '__main__' :
    app.run( debug=True, port=8080)




# activate DEBUG mode
# FLASK_APP=restful.py FLASK_DEBUG=1 python -m flask run