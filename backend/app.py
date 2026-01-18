from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'wedding.db')

def init_db():
    """Initialize the database with the RSVP table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rsvp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            guests INTEGER NOT NULL,
            attending TEXT NOT NULL,
            dietary TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

@app.route('/api/rsvp', methods=['POST'])
def create_rsvp():
    """Create a new RSVP entry"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'guests', 'attending']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Insert into database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO rsvp (name, email, phone, guests, attending, dietary, message)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['name'],
            data['email'],
            data.get('phone', ''),
            data['guests'],
            data['attending'],
            data.get('dietary', ''),
            data.get('message', '')
        ))
        
        conn.commit()
        rsvp_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'message': 'RSVP submitted successfully',
            'id': rsvp_id
        }), 201
        
    except Exception as e:
        print(f"Error creating RSVP: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/rsvp', methods=['GET'])
def get_rsvps():
    """Get all RSVP entries"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM rsvp ORDER BY created_at DESC')
        rows = cursor.fetchall()
        
        rsvps = []
        for row in rows:
            rsvps.append({
                'id': row['id'],
                'name': row['name'],
                'email': row['email'],
                'phone': row['phone'],
                'guests': row['guests'],
                'attending': row['attending'],
                'dietary': row['dietary'],
                'message': row['message'],
                'created_at': row['created_at']
            })
        
        conn.close()
        return jsonify(rsvps), 200
        
    except Exception as e:
        print(f"Error fetching RSVPs: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/rsvp/<int:rsvp_id>', methods=['GET'])
def get_rsvp(rsvp_id):
    """Get a single RSVP entry by ID"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM rsvp WHERE id = ?', (rsvp_id,))
        row = cursor.fetchone()
        
        if row is None:
            return jsonify({'error': 'RSVP not found'}), 404
        
        rsvp = {
            'id': row['id'],
            'name': row['name'],
            'email': row['email'],
            'phone': row['phone'],
            'guests': row['guests'],
            'attending': row['attending'],
            'dietary': row['dietary'],
            'message': row['message'],
            'created_at': row['created_at']
        }
        
        conn.close()
        return jsonify(rsvp), 200
        
    except Exception as e:
        print(f"Error fetching RSVP: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get RSVP statistics"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Total RSVPs
        cursor.execute('SELECT COUNT(*) FROM rsvp')
        total = cursor.fetchone()[0]
        
        # Attending
        cursor.execute('SELECT COUNT(*) FROM rsvp WHERE attending = "yes"')
        attending = cursor.fetchone()[0]
        
        # Not attending
        cursor.execute('SELECT COUNT(*) FROM rsvp WHERE attending = "no"')
        not_attending = cursor.fetchone()[0]
        
        # Total guests
        cursor.execute('SELECT SUM(guests) FROM rsvp WHERE attending = "yes"')
        total_guests = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return jsonify({
            'total_rsvps': total,
            'attending': attending,
            'not_attending': not_attending,
            'total_guests': total_guests
        }), 200
        
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    init_db()
    print("Starting Flask server on http://localhost:5000")
    app.run(debug=True, port=5000)
