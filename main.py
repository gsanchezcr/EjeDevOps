from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sumar', methods=['GET'])
def suma():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    resultado = a + b
    return jsonify({'resultado': resultado})

@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    datos = request.get_json()
    a = data.get('a', 1)
    b = data.get('b', 1)
    resultado = a * b
    return jsonify({'resultado': resultado})