from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  

# Sample route
@app.route('/')
def home():
    return "API Server is running!"

# Example GET API
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# Example POST API
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(debug=True, port=5500)
