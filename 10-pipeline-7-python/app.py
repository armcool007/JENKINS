from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# Database path (use environment variable for flexibility)
DB_PATH = os.getenv('DATABASE_URL', 'app.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Python DB App!"})

@app.route('/users', methods=['GET', 'POST'])
def users():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        return jsonify({"message": "User added"}), 201
    else:
        users = conn.execute('SELECT * FROM users').fetchall()
        return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    # Initialize DB if it doesn't exist
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    conn.commit()
    conn.close()
    app.run(host='0.0.0.0', port=5000)
