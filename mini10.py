## Configuración de Base de Datos para un Microservicio: Define un esquema de base de datos para un microservicio que gestione productos. Luego, escribe un script SQL simple para crear la tabla correspondiente y conectar el microservicio a la base de datos (puede ser SQLite para simplificar).

##  Script SQL para crear la tabla products
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
);



## Scriptapp.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Ruta para crear la tabla de productos (solo para inicializar)
@app.before_first_request
def initialize_database():
    with sqlite3.connect('products.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        conn.commit()

# Endpoint para agregar un nuevo producto
@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description', '')
    price = data.get('price')
    stock = data.get('stock')

    if not (name and price is not None and stock is not None):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    with sqlite3.connect('products.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, description, price, stock)
            VALUES (?, ?, ?, ?)
        ''', (name, description, price, stock))
        conn.commit()
        product_id = cursor.lastrowid

    return jsonify({'message': f'Producto {product_id} agregado correctamente'}), 201

# Endpoint para obtener todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    with sqlite3.connect('products.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        products = [{'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'stock': row[4]} for row in rows]

    return jsonify(products), 200

if __name__ == "__main__":
    app.run(debug=True)
