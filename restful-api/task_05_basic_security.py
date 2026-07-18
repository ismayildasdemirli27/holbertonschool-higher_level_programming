#!/usr/bin/python3
"""API Security and Authentication Techniques."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Use a strong secret in production
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- Basic Authentication ---

@auth.verify_password
def verify_password(username, password):
    """Verifies user credentials for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user.get('password'), password):
        return username
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """A protected route requiring Basic Auth."""
    return "Basic Auth: Access Granted"

# --- JWT Authentication ---

@app.route('/login', methods=['POST'])
def login():
    """Authenticates a user and returns a JWT."""
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    user = users.get(username)
    if user and check_password_hash(user.get('password'), password):
        # Embed the role in the access token along with the username
        access_token = create_access_token(identity={"username": username, "role": user.get('role')})
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """A protected route requiring a valid JWT."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """A protected route requiring a valid JWT with admin role."""
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- Custom JWT Error Handlers ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
