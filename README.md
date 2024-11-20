# Bakery Management System

A simple Python-based Bakery Management System with a Flask backend and a script for managing orders.

## Features

- Add new orders with automatically generated Order ID and current date.
- Retrieve details of an existing order by Order ID.
- Update an existing order's details.
- List all orders.
- Export orders to an Excel file (optional).

## Technologies Used

- **Backend**: Flask
- **Database**: SQLite
- **Frontend Script**: Python with Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sourav072/bakery_management_system.git
   cd bakery-management-system
2. Create and activate a virtual environment:

  On Windows:
            python -m venv venv
            venv\Scripts\activate

  On macOS/Linux:
            python3 -m venv venv
            source venv/bin/activate

3. Install dependencies:
            pip install -r requirements.txt
   
4.  Start the backend server:
            cd backend
            python app.py

5. Run the script:
            cd ../scripts
            python bakery_management_system.py

API Endpoints:
Method        	Endpoint        	Description
POST	          /orders	          Add a new order
GET	            /orders/<id>	    Retrieve an order
PUT	            /orders/<id>	    Update an existing order
GET	            /orders	          List all orders

License: 
This project is licensed under the MIT License. See the LICENSE file for details.
