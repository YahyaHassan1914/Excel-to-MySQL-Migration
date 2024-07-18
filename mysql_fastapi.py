from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, inspect, text
import configparser
from typing import Dict, Any, List

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Database connection parameters
db_user = config['mysql']['user']
db_password = config['mysql']['password']
db_host = config['mysql']['host']
db_name = config['mysql']['database']

# Create a database engine
DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(DATABASE_URL)

# Create a FastAPI instance
app = FastAPI()

@app.get("/tables")
def read_tables():
    try:
        # Inspect the database
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tables/{table_name}")
def read_table(table_name: str) -> Dict[str, Any]:
    try:
        # Check if the table exists
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        if table_name not in tables:
            raise HTTPException(status_code=404, detail="Table not found")
        
        # Fetch table data
        query = f"SELECT * FROM {table_name}"
        with engine.connect() as connection:
            result = connection.execute(text(query))
            columns = result.keys()
            data = [dict(zip(columns, row)) for row in result]
        
        return {"table_name": table_name, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the app, use the command: uvicorn main:app --reload
