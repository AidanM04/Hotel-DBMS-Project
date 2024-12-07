from flask import Blueprint, request, jsonify
from models import db, Room

room_bp = Blueprint('room_bp', __name__)

# Create a new room
@room_bp.route('/add_room', methods=['POST'])
def add_room():
    try:
        data = request.json
        new_room = Room(
            roomType=data['roomType'],
            roomNumber=data['roomNumber'],
            roomFloor=data['roomFloor'],
            pricePerNight=data['pricePerNight'],
            description=data['description']
        )
        db.session.add(new_room)
        db.session.commit()
        return jsonify({"message": "Room added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all rooms
@room_bp.route('/rooms', methods=['GET'])
def get_rooms():
    try:
        rooms = Room.query.all()
        result = [
            {
                "roomID": room.roomID,
                "roomType": room.roomType,
                "roomNumber": room.roomNumber,
                "roomFloor": room.roomFloor,
                "pricePerNight": str(room.pricePerNight),
                "description": room.description
            }
            for room in rooms
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#update all rooms
@room_bp.route('/update_room/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    try:
        data = request.json
        room = Room.query.get(room_id)
        if not room:
            return jsonify({"error": "Room not found"}), 404

        room.roomType = data.get('roomType', room.roomType)
        room.roomNumber = data.get('roomNumber', room.roomNumber)
        room.roomFloor = data.get('roomFloor', room.roomFloor)
        room.pricePerNight = data.get('pricePerNight', room.pricePerNight)
        room.description = data.get('description', room.description)

        db.session.commit()
        return jsonify({"message": "Room updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# delete rooms
@room_bp.route('/delete_room/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    try:
        room = Room.query.get(room_id)
        if not room:
            return jsonify({"error": "Room not found"}), 404

        db.session.delete(room)
        db.session.commit()
        return jsonify({"message": "Room deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
