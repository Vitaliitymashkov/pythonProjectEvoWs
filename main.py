# This is a task 2 - WS for Evo
import sqlite3

import web
from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.exceptions import abort
import os
port = int(os.environ.get("PORT", 8080))

urls = ('/index', 'index')
app = web.application(urls, globals())

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfghjkl'


@app.route("/")
def index():
    return render_template('index.html')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/users')
def users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('users.html', users=users)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']

        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()

            users = conn.execute('SELECT * FROM users WHERE name = ?', (name,)).fetchall()
            if users:
                flash('Вже бачилися, ' + name, 'info')
            else:
                conn.execute('INSERT INTO users (name) VALUES (?)',
                             (name,))
                flash('Привіт, ' + name, 'info')
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
