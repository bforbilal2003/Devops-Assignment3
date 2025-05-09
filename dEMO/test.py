import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)
db_path = "users.db"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 🚨 SQL Injection vulnerability
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful"
    else:
        return "Login failed"

@app.route('/delete', methods=['POST'])
def delete_file():
    filename = request.form['filename']

    # 🚨 Arbitrary file deletion vulnerability (Path Traversal)
    os.remove(f"/var/data/{filename}")

    return "File deleted"
