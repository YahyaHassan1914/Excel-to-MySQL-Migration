import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import configparser

# Load the Excel file
df = pd.read_excel('items.xlsx')
print(df)

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Database connection parameters
# Get the database connection parameters
db_user = config['mysql']['user']
db_password = config['mysql']['password']
db_host = config['mysql']['host']
db_name = config['mysql']['database']

# Create an engine object
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')

# Insert the data into the MySQL table
df.to_sql('items_table', con=engine, if_exists='replace', index=True)

print("Data saved successfully!")