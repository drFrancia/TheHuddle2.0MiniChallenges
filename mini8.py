## Autenticación Básica con JWT: Implementa un proceso simple para generar y validar un token JWT en una aplicación. Este token debería contener un ID de usuario y una fecha de expiración, y tu aplicación debería rechazar cualquier solicitud que no incluya un token válido.

from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = 'PASS_SECRET'

def generate_token(user_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token válido por 1 hora
    token = jwt.encode({
        'user_id': user_id,
        'exp': expiration_time
    }, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado'}
    except jwt.InvalidTokenError:
        return {'error': 'Token inválido'}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('user_id')
    if user_id:
        token = generate_token(user_id)
        return jsonify({'token': token})
    return jsonify({'error': 'Falta el ID de usuario'}), 400

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if token:
        token = token.replace('Bearer ', '')
        decoded_token = verify_token(token)
        if 'error' in decoded_token:
            return jsonify(decoded_token), 401
        return jsonify({'message': 'Acceso concedido', 'user_id': decoded_token['user_id']})
    return jsonify({'error': 'Token requerido'}), 401

if __name__ == "__main__":
    app.run(debug=True)
