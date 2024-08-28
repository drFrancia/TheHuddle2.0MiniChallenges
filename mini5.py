# Creación de un Endpoint para Recibir Logs: Implementa un servidor básico con un solo endpoint /logs que acepte solicitudes POST y simplemente almacene los logs recibidos en una lista en memoria.

from flask import Flask, request, jsonify

app = Flask(__name__)
logs = []

@app.route('/logs', methods=['POST'])
def receive_log():
    log_entry = request.get_json()
    
    if not log_entry or not isinstance(log_entry, dict):
        return jsonify({"error": "formato Invsalido de log"}), 400
    
    logs.append(log_entry)
    
    return jsonify({"estado": "Log recibido"}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs), 200

if __name__ == "__main__":
    app.run(debug=True)
