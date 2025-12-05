from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" for users
# Key: username, Value: dictionary of user details
users = {}

@app.route('/')
def home():
    """
    Root endpoint.
    Returns a welcome message.
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """
    Returns a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """
    Returns the status of the API.
    """
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    If not found, returns a 404 error.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user.
    Expects JSON data.
    """
    # Attempt to parse JSON. silent=True returns None if parsing fails.
    try:
        data = request.get_json()
    except Exception:
        data = None

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Add new user to the dictionary
    users[username] = data
    
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
