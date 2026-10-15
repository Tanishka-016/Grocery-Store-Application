# Grocery Store Management Application

A web-based grocery store management application built as part of the Codebasics project tutorial. It helps manage grocery products and customer orders.

## Features

- Manage grocery products
- View and manage customer orders
- Organize products by unit of measurement
- Web-based user interface
- Backend API connected to a MySQL database

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap, jQuery
- **Backend:** Python, Flask
- **Database:** MySQL

## Project Structure

```text
Grocery_App/
├── Backend/
│   ├── server.py
│   ├── sql_connection.py
│   ├── products_dao.py
│   ├── orders_dao.py
│   └── uom_dao.py
├── ui/
│   ├── css/
│   ├── images/
│   ├── js/
│   ├── index.html
│   ├── manage-product.html
│   └── order.html
└── README.md
```

## Prerequisites

- Python 3
- MySQL Server
- pip
- A web browser

## Setup and Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Tanishka-016/Grocery-Store-Application.git
   cd Grocery-Store-Application
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the Python dependencies required by the project. If a `requirements.txt` file is available, run:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your MySQL database and update the database connection settings for your local environment.

5. Start the backend using the appropriate command for your Flask application. For example:

   ```bash
   python Backend/server.py
   ```

6. Serve the frontend from the `ui` directory using a local web server and configure it to communicate with the backend.

**Note:** Database setup, required dependencies, and frontend/backend configuration may vary according to your local setup.

## Learning Project

This project was completed while following the Codebasics grocery store application tutorial and is intended for learning and practice.
