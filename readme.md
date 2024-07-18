# Data Migration and Viewing Application

## Overview

This repository contains two main components:

1. **Excel to MySQL Data Migration**: A Python program to migrate data from an Excel file to a MySQL database.
2. **FastAPI Application**: A FastAPI service to view tables and their data from a MySQL database.

## Excel to MySQL Data Migration

### Overview

This part of the project demonstrates how to:

- Load data from an Excel file into a pandas DataFrame.
- Connect to a MySQL database using SQLAlchemy.
- Insert data from the DataFrame into a MySQL table.

### Requirements

- Python 3.x
- pandas
- openpyxl
- mysql-connector-python
- sqlalchemy

Install the required Python packages:

```
pip install pandas openpyxl mysql-connector-python sqlalchemy
```

### Configuration

Update the config.ini file with your MySQL database connection details:

```
[mysql]
user = your_actual_username
password = your_actual_password
host = your_actual_host
database = your_database_name
```

### Usage

1. Place your Excel file in the project directory.
2. Update the excel_to_mysql.py script with the appropriate table name and other configurations.
3. Run the script:

```
python excel_to_mysql.py
```

## FastAPI Application

### Overview

This component demonstrates how to create a FastAPI application to view tables and their data from a MySQL database.

### Requirements

- Python 3.x
- fastapi
- uvicorn
- sqlalchemy
- mysql-connector-python

Install the required Python packages:

```
pip install fastapi uvicorn sqlalchemy mysql-connector-python
```

### Configuration

Update the config.ini file with your MySQL database connection details (same as for migration).

### Usage

1. Save the FastAPI script as main.py.
2. Run the FastAPI application:

```
uvicorn main:app --reload
```

### Access the API Endpoints

- Get list of tables:

```
http://127.0.0.1:8000/tables
```

- Get data from a specific table:

```
http://127.0.0.1:8000/tables/{table_name}
```

Replace `{table_name}` with the name of the table you want to view.

### Example

Here’s an example config.ini file for both migration and viewing:

```
[mysql]
user = admin
password = admin123
host = localhost
database = inventory_db
```

## Contact

For the complete project or if you need assistance, please contact us at:

Email: yahyahassanmohamed1914@gmail.com

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
