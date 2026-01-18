from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'wedding.db')

def send_confirmation_email(name, email, attending, guests):
    """Send RSVP confirmation email"""
    try:
        msg = Message(
            subject='RSVP Confirmation - The Kendalls Wedding',
            sender=('Alex and Alesia', os.environ.get('MAIL_USERNAME')),
            recipients=[email],
            reply_to='noreply@kendallwedding.com'
        )
        
        status = "attending" if attending == "yes" else "unable to attend"
        guest_text = f"{guests} guest{'s' if guests > 1 else ''}"
        
        msg.body = f"""Dear {name},

Thank you for your RSVP!

We have received your response and you are confirmed as {status} with {guest_text}.

Wedding Details:
Date: March 27, 2027
Venue: The Grand Ballroom

If you need to update your RSVP, please visit our website.

We look forward to celebrating with you!

With love,
The Kendalls
"""
        
        msg.html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                <h1 style="color: #1a1a1a; font-family: 'Georgia', serif;">The Kendalls Wedding</h1>
                <p>Dear {name},</p>
                <p>Thank you for your RSVP!</p>
                <p>We have received your response and you are confirmed as <strong>{status}</strong> with <strong>{guest_text}</strong>.</p>
                
                <div style="background: #f5f5f5; padding: 15px; margin: 20px 0; border-left: 4px solid #1a1a1a;">
                    <h3 style="margin-top: 0;">Wedding Details</h3>
                    <p style="margin: 5px 0;"><strong>Date:</strong> March 27, 2027</p>
                    <p style="margin: 5px 0;"><strong>Venue:</strong> The Grand Ballroom</p>
                </div>
                
                <p>If you need to update your RSVP, please visit our website.</p>
                <p>We look forward to celebrating with you!</p>
                
                <p style="margin-top: 30px;">With love,<br><strong>The Kendalls</strong></p>
            </div>
        </body>
        </html>
        """
        
        mail.send(msg)
        print(f"Confirmation email sent to {email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


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
        
        # Send confirmation email
        send_confirmation_email(
            data['name'],
            data['email'],
            data['attending'],
            data['guests']
        )
        
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

@app.route('/api/rsvp/check', methods=['POST'])
def check_rsvp():
    """Check if an RSVP already exists by email or phone"""
    try:
        data = request.get_json()
        email = data.get('email')
        phone = data.get('phone')
        
        if not email and not phone:
            return jsonify({'exists': False}), 200
        
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Check by email or phone
        if email and phone:
            cursor.execute('SELECT * FROM rsvp WHERE LOWER(email) = LOWER(?) OR phone = ?', (email, phone))
        elif email:
            cursor.execute('SELECT * FROM rsvp WHERE LOWER(email) = LOWER(?)', (email,))
        elif phone:
            cursor.execute('SELECT * FROM rsvp WHERE phone = ?', (phone,))
        
        row = cursor.fetchone()
        
        if row is None:
            conn.close()
            return jsonify({'exists': False}), 200
        
        rsvp = {
            'exists': True,
            'id': row['id'],
            'name': row['name'],
            'email': row['email'],
            'phone': row['phone'],
            'guests': row['guests'],
            'attending': row['attending'],
            'created_at': row['created_at']
        }
        
        conn.close()
        return jsonify(rsvp), 200
        
    except Exception as e:
        print(f"Error checking RSVP: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/rsvp/find', methods=['GET'])
def find_rsvp():
    """Find an RSVP by email, name, or phone"""
    try:
        email = request.args.get('email')
        name = request.args.get('name')
        phone = request.args.get('phone')
        
        if not email and not name and not phone:
            return jsonify({'error': 'Please provide email, name, or phone number'}), 400
        
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Try to find by email first (most reliable)
        if email:
            cursor.execute('SELECT * FROM rsvp WHERE LOWER(email) = LOWER(?)', (email,))
        elif name:
            cursor.execute('SELECT * FROM rsvp WHERE LOWER(name) = LOWER(?)', (name,))
        elif phone:
            cursor.execute('SELECT * FROM rsvp WHERE phone = ?', (phone,))
        
        row = cursor.fetchone()
        
        if row is None:
            return jsonify({'error': 'RSVP not found. Please check your information and try again.'}), 404
        
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
        print(f"Error finding RSVP: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/rsvp/<int:rsvp_id>', methods=['PUT'])
def update_rsvp(rsvp_id):
    """Update an existing RSVP entry"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'guests', 'attending']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Check if RSVP exists
        cursor.execute('SELECT id FROM rsvp WHERE id = ?', (rsvp_id,))
        if cursor.fetchone() is None:
            conn.close()
            return jsonify({'error': 'RSVP not found'}), 404
        
        # Update the RSVP
        cursor.execute('''
            UPDATE rsvp 
            SET name = ?, email = ?, phone = ?, guests = ?, attending = ?, dietary = ?, message = ?
            WHERE id = ?
        ''', (
            data['name'],
            data['email'],
            data.get('phone', ''),
            data['guests'],
            data['attending'],
            data.get('dietary', ''),
            data.get('message', ''),
            rsvp_id
        ))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'message': 'RSVP updated successfully',
            'id': rsvp_id
        }), 200
        
    except Exception as e:
        print(f"Error updating RSVP: {e}")
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
