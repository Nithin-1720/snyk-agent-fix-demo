from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")

    query = (
        "SELECT * FROM users WHERE username='"
        + username +
        "'"
    )

    return str(conn.execute(query).fetchall())
