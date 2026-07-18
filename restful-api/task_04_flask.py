#!/usr/bin/python3
"""A simple API using Flask."""
from flask import Flask, jsonify, request


app = Flask(__name__)

# Yoxlayıcı (checker) üçün başlanğıcda boş olmalıdır
users = {}


@app.route("/")
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object corresponding to the provided username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary."""
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
