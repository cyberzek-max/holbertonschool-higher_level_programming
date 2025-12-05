from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Security Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key-please-change"  # Change this for production!

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ==========================================
# 1. Basic Authentication Setup
# ==========================================

@auth.verify_password
def verify_password(username, password):
    """
    Callback for Basic Auth to verify credentials.
    Returns the username if valid, None otherwise.
    """
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Endpoint protected by Basic Auth.
    """
    return "Basic Auth: Access Granted"

# ==========================================
# 2. JWT Error Handling (Strict 401s)
# ==========================================

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(header, payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(header, payload):
    return jsonify({"error": "Fresh token required"}), 401

# ==========================================
# 3. JWT Authentication Endpoints
# ==========================================

@app.route('/login', methods=['POST'])
def login():
    """
    Accepts username/password, validates them, and returns a JWT access token.
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    username = data.get("username")
    password = data.get("password")

    # Validate user exists and password is correct
    if username in users and \
            check_password_hash(users[username]["password"], password):
        
        # Create a token with the username as the identity
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT. Requires a valid Bearer token.
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Endpoint protected by JWT + Role Check.
    Only allows users with role 'admin'.
    """
    # Get the identity (username) from the current token
    current_user_id = get_jwt_identity()
    
    # Retrieve the user dictionary from memory
    user = users.get(current_user_id)
    
    # Check if user exists and has admin role
    if user and user["role"] == "admin":
        return "Admin Access: Granted"
    
    # If not admin, return 403 Forbidden
    return jsonify({"error": "Admin access required"}), 403

if __name__ == '__main__':
    app.run()
