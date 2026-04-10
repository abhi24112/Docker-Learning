import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host='db',
        database='mydb',
        user='user',
        password='password'
    )

    return conn