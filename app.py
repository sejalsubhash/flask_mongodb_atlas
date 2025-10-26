import os
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# MongoDB Atlas connection string (from environment variable or directly)
MONGO_URI = os.getenv('MONGO_URI')
# Connect to MongoDB Atlas
mongo_client = None
if MONGO_URI:
    try:
        mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        _ = mongo_client.server_info()  # test connection
        db = mongo_client.get_database()  # uses default DB from URI
        collection = db.get_collection('submissions')
    except Exception as e:
        print("Warning: Could not connect to MongoDB Atlas:", e)
        mongo_client = None
        collection = None
else:
    collection = None

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# API route: read local data.json and return as JSON
@app.route('/api')
def api_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to accept form submissions
@app.route('/submit', methods=['POST'])
def submit():
    payload = request.get_json()
    if not payload:
        return jsonify({'ok': False, 'error': 'No JSON payload received.'}), 400

    name = payload.get('name')
    email = payload.get('email')

    if not name or not email:
        return jsonify({'ok': False, 'error': 'Name and email are required.'}), 400

    if collection is None:
        return jsonify({'ok': False, 'error': 'Database not configured.'}), 500

    try:
        doc = {'name': name, 'email': email}
        result = collection.insert_one(doc)
        return jsonify({'ok': True, 'id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
