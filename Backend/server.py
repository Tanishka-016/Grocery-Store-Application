from flask import Flask, jsonify, request
from Backend import uom_dao
import products_dao
import uom_dao
import json
from sql_connection import get_sql_connection
import orders_dao

app = Flask(__name__)
connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uoms():
    uoms = uom_dao.get_uoms(connection)
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getOrders', methods=['GET'])
def get_orders():
    orders = orders_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProducts', methods=['POST'])
def delete_products():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id,
        "message": "Product deleted successfully"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request .form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id,
        "message": "Product inserted successfully"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/editProduct', methods=['POST'])
def edit_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.edit_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id,
        "message": "Product updated successfully"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting the Flask server...")
    app.run(port=5000)

