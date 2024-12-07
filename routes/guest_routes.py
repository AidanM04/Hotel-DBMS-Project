from flask import Blueprint, request, jsonify
from models import db, Guest

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/add_guest', methods=['POST'])
def add_guest():
    try:
        # Parse JSON data
        data = request.get_json() or {}
        
        # Validate required keys
        required_keys = ['first_name', 'last_name', 'email', 'phone']
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing required data fields"}), 400

        # Create a new guest object
        new_guest = Guest(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone=data['phone']
        )
        
        # Add to database
        db.session.add(new_guest)
        db.session.commit()
        
        return jsonify({"message": "Guest added successfully!"}), 201
    except Exception as e:
        # Detailed error response
        return jsonify({"error": f"Failed to add guest: {str(e)}"}), 400


@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    try:
        guests = Guest.query.all()  # Fetch all guests from the database
        guests_list = [
            {"id": guest.guestID, "first_name": guest.first_name, "last_name": guest.last_name, "email": guest.email, "phone": guest.phone}
            for guest in guests
        ]
        return jsonify(guests_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@guest_bp.route('/update_guest/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
    try:
        data = request.json
        guest = Guest.query.get(guest_id)
        if not guest:
            return jsonify({"error": "Guest not found"}), 404
        
        # Update guest details
        guest.first_name = data.get('first_name', guest.first_name)
        guest.last_name = data.get('last_name', guest.last_name)
        guest.email = data.get('email', guest.email)
        guest.phone = data.get('phone', guest.phone)

        db.session.commit()
        return jsonify({"message": "Guest updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@guest_bp.route('/delete_guest/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id):
    try:
        guest = Guest.query.get(guest_id)
        if not guest:
            return jsonify({"error": "Guest not found"}), 404

        db.session.delete(guest)
        db.session.commit()
        return jsonify({"message": "Guest deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
