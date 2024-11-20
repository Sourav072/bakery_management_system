import requests
from datetime import datetime
import uuid

BASE_URL = "http://127.0.0.1:5000"

# Function to generate a unique order ID
def generate_order_id():
    return str(uuid.uuid4())[:8]  # Generates a short unique ID (e.g., 'f47ac10b')

# Function to add a new order via the backend
def add_order(customer_name, quantity):
    order_id = generate_order_id()  # Automatically generate order ID
    order_date = datetime.now().strftime("%Y-%m-%d")  # Automatically fetch current date
    data = {
        "id": order_id,
        "customer_name": customer_name,
        "quantity": quantity,
        "order_date": order_date
    }
    response = requests.post(f"{BASE_URL}/orders", json=data)
    if response.status_code == 201:
        print(f"Order added successfully! Order ID: {order_id}")
    else:
        print(f"Error: {response.json()['message']}")

# Function to retrieve an order via the backend
def get_order(order_id):
    response = requests.get(f"{BASE_URL}/orders/{order_id}")
    if response.status_code == 200:
        print("\nOrder Details:")
        print(response.json())
    else:
        print(f"Error: {response.json()['message']}")

# Function to update an existing order via the backend
def update_order(order_id):
    customer_name = input("Enter new Customer Name (leave blank to keep unchanged): ")
    quantity = input("Enter new Quantity (leave blank to keep unchanged): ")
    order_date = input("Enter new Order Date (YYYY-MM-DD, leave blank to keep unchanged): ")

    data = {}
    if customer_name:
        data["customer_name"] = customer_name
    if quantity:
        try:
            data["quantity"] = int(quantity)
        except ValueError:
            print("Invalid quantity. Skipping update for quantity.")
    if order_date:
        data["order_date"] = order_date

    response = requests.put(f"{BASE_URL}/orders/{order_id}", json=data)
    if response.status_code == 200:
        print("Order updated successfully!")
    else:
        print(f"Error: {response.json()['message']}")

# Function to list all orders via the backend
def list_orders():
    response = requests.get(f"{BASE_URL}/orders")
    if response.status_code == 200:
        orders = response.json()
        if orders:
            print("\nAll Orders:")
            for order in orders:
                print(order)
        else:
            print("No orders found.")
    else:
        print("Error fetching orders.")

# Main menu for the Bakery Management System
if __name__ == "__main__":
    while True:
        print("\n--- Bakery Management System ---")
        print("1. Add a new order")
        print("2. Retrieve an order")
        print("3. Update an order")
        print("4. List all orders")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            customer_name = input("Enter Customer Name: ")
            quantity = int(input("Enter Quantity: "))
            add_order(customer_name, quantity)

        elif choice == "2":
            order_id = input("Enter Order ID to retrieve: ")
            get_order(order_id)

        elif choice == "3":
            order_id = input("Enter Order ID to update: ")
            update_order(order_id)

        elif choice == "4":
            list_orders()

        elif choice == "5":
            print("Exiting Bakery Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
