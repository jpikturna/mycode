#!/user/bin/env python3
"""Project 3:  Utilizing Flask; Script One: Setting up the API"""

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import session
import sqlite3

app = Flask(__name__)


# Create two mock users with Integer id's and String names
data = {
    "message": "Welcome to the Flask API. Isn't that just neat?!",
    "users": [
        {"id": 1, "name": "Eric"},
        {"id": 2, "name": "Michael"}
    ]
}

# Home endpoint, returns HTML
@app.route('/')
def home():
    return render_template('index.html')

# JSON endpoint
@app.route('/json')
def json_endpoint():
    return jsonify(data)

# Require a session value to move forward
@app.route('/protected')
def protected_endpoint():
    """self-explanatory function (protect an endpoint using sessions)"""
    if 'user_id' in session:
        user_id = session['user_id']
        return f"Welcome, User ID: {user_id}"
    else:
        return "Nice try, dude. Please.... just log in."

# SQLite3 database
def create_table():
    """creates a table based on the data dictionary"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

def insert_user(name):
    """Populates the above table with id and name values from the 'data' dictionary above"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

@app.route('/add_user/<name>')
def add_user(name):
    insert_user(name)
    return f"User {name} brought into the fold."

if __name__ == '__main__':
    create_table()
    app.run(host="0.0.0.0", port=2224)

