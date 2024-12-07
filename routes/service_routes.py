from flask import Blueprint, request, jsonify
from models import db, Service

service_bp = Blueprint('service_bp', __name__)

# POST endpoint to add a service
@service_bp.route('/add_service', methods=['POST'])
def add_service():
    try:
        data = request.json
        new_service = Service(
            serviceName=data['serviceName'],
            servicePrice=data['servicePrice'],
            description=data.get('description')  # Optional
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({"message": "Service added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET endpoint to fetch all services
@service_bp.route('/get_services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        services_list = [
            {
                "serviceID": service.serviceID,
                "serviceName": service.serviceName,
                "servicePrice": float(service.servicePrice),
                "description": service.description
            }
            for service in services
        ]
        return jsonify(services_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
