from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Model API is running 🚀"}

@app.get("/data")
def read_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM test;")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": data}

@app.post("/insert_data")
def insert():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO test (name) VALUES ('Abhishek');")
    conn.commit()

    cursor.close()
    conn.close()
    
    return {"message": "Data inserted successfully"}