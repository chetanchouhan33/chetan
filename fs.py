from flask import Flask
import sqlite3

app = Flask(__name__)

# Create database and table
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  age INTEGER)''')
    conn.commit()
    conn.close()


# Insert user
def insert_user(name, email, age):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
              (name, email, age))
    conn.commit()
    conn.close()


# Show users
def get_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users


# Create table when app starts
create_table()


@app.route('/')
def home():
    return "Flask + SQLite is running!"


@app.route('/add')
def add():
    insert_user('John Doe', 'johndoe@example.com', 30)
    return "User inserted successfully!"


@app.route('/users')
def users():
    data = get_users()
    return str(data)


if __name__ == '__main__':
    app.run(debug=True)
