from flask import Blueprint, request, jsonify
from models import db, Booking

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/add_booking', methods=['POST'])
def add_booking():
    try:
        data = request.json
        new_booking = Booking(
            roomID=data['roomID'],
            guestID=data['guestID'],
            checkInDate=data['checkInDate'],
            checkOutDate=data['checkOutDate'],
            paymentStatus=data.get('paymentStatus', 'pending')
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#read
@booking_bp.route('/get_bookings', methods=['GET'])
def get_all_bookings():
    try:
        bookings = Booking.query.all()
        booking_list = []
        for booking in bookings:
            booking_list.append({
                "bookingID": booking.bookingID,
                "roomID": booking.roomID,
                "guestID": booking.guestID,
                "checkInDate": booking.checkInDate,
                "checkOutDate": booking.checkOutDate,
                "paymentStatus": booking.paymentStatus
            })
        return jsonify(booking_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


 # update booking   
@booking_bp.route('/update_booking/<int:bookingID>', methods=['PUT'])
def update_booking(bookingID):
    try:
        data = request.json
        booking = Booking.query.get(bookingID)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Update the fields
        booking.roomID = data.get("roomID", booking.roomID)
        booking.guestID = data.get("guestID", booking.guestID)
        booking.checkInDate = data.get("checkInDate", booking.checkInDate)
        booking.checkOutDate = data.get("checkOutDate", booking.checkOutDate)
        booking.paymentStatus = data.get("paymentStatus", booking.paymentStatus)

        db.session.commit()
        return jsonify({"message": "Booking updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@booking_bp.route('/delete_booking/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    try:
        booking = Booking.query.get(booking_id)
        if not booking:
            return jsonify({"error": f"Booking with ID {booking_id} not found"}), 404

        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": f"Booking with ID {booking_id} deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
