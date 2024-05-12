#flask to RDS

from flask import Flask
import psycopg2

app = Flask(__name__)

# Database connection details
DB_ENDPOINT = 'nebula-db.cd2ae4g4q9fu.us-east-2.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'nebula-db'
DB_USER = '504232514998'
DB_PASSWORD = 'Creativity1'



# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_ENDPOINT,
        port=DB_PORT
    )
    print("Connected to the database")
except Exception as e:
    print("Error connecting to the database:", e)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '_main_':
    app.run(debug=True)