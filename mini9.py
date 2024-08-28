## Creación de un Endpoint RESTful Sencillo: Implementa un endpoint básico en un microservicio usando Python (Flask) o Node.js (Express). El endpoint debería recibir un ID de producto y devolver un mensaje simple (ejemplo: "Producto [ID] consultado correctamente").

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    message = f"Producto {product_id} consultado correctamente"
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
