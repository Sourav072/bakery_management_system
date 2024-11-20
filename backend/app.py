from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('bakery.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id TEXT PRIMARY KEY,
                        customer_name TEXT,
                        quantity INTEGER,
                        order_date TEXT
                    )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "<h1>Welcome to the Bakery Management System API</h1><p>Use the appropriate endpoints to interact with the system.</p>"

@app.route('/favicon.ico')
def favicon():
    return "", 204

# Add a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    conn = sqlite3.connect('bakery.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (id, customer_name, quantity, order_date) VALUES (?, ?, ?, ?)",
                   (data['id'], data['customer_name'], data['quantity'], data['order_date']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Order created successfully!"}), 201

# Get an order by ID
@app.route('/orders/<id>', methods=['GET'])
def get_order(id):
    conn = sqlite3.connect('bakery.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (id,))
    order = cursor.fetchone()
    conn.close()
    if order:
        return jsonify({"id": order[0], "customer_name": order[1], "quantity": order[2], "order_date": order[3]})
    else:
        return jsonify({"message": "Order not found"}), 404

# Update an order by ID
@app.route('/orders/<id>', methods=['PUT'])
def update_order(id):
    data = request.json
    conn = sqlite3.connect('bakery.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (id,))
    order = cursor.fetchone()
    if not order:
        return jsonify({"message": "Order not found"}), 404

    cursor.execute("""UPDATE orders
                      SET customer_name = COALESCE(?, customer_name),
                          quantity = COALESCE(?, quantity),
                          order_date = COALESCE(?, order_date)
                      WHERE id = ?""",
                   (data.get('customer_name'), data.get('quantity'), data.get('order_date'), id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Order updated successfully!"})

# Export all orders to JSON
@app.route('/orders', methods=['GET'])
def list_orders():
    conn = sqlite3.connect('bakery.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return jsonify([{"id": order[0], "customer_name": order[1], "quantity": order[2], "order_date": order[3]} for order in orders])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
