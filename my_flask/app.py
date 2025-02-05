from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client['user_registration']
users_collection = db['users']

@app.route('/')
def index():
    return render_template('reg.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        gender = request.form.get('gender')

        # Validation
        if not name or not email or not phone or not gender:
            return jsonify({'error': 'All fields are required'}), 400

        # Insert into MongoDB
        user = {
            'name': name,
            'email': email,
            'phone': phone,
            'gender': gender
        }
        users_collection.insert_one(user)
        return jsonify({'message': 'Registration Successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)