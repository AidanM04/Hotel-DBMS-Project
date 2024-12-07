from flask import Blueprint, request, jsonify
from models import db, BookingServices

booking_service_bp = Blueprint('booking_service_bp', __name__)

# POST endpoint to add a booking-service relation
@booking_service_bp.route('/add_booking_service', methods=['POST'])
def add_booking_service():
    try:
        data = request.json
        new_booking_service = BookingServices(
            bookingID=data['bookingID'],
            serviceID=data['serviceID'],
            quantity=data['quantity']
        )
        db.session.add(new_booking_service)
        db.session.commit()
        return jsonify({"message": "Booking-Service relation added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET endpoint to fetch all booking-service relations
@booking_service_bp.route('/get_booking_services', methods=['GET'])
def get_booking_services():
    try:
        booking_services = BookingServices.query.all()
        booking_services_list = [
            {
                "bookingID": bs.bookingID,
                "serviceID": bs.serviceID,
                "quantity": bs.quantity
            }
            for bs in booking_services
        ]
        return jsonify(booking_services_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
