from flask import Blueprint, request, jsonify
from models import db, Payment

payment_bp = Blueprint('payment_bp', __name__)


# POST endpoint to add a payment
@payment_bp.route('/add_payment', methods=['POST'])
def add_payment():
    try:
        data = request.json
        new_payment = Payment(
            bookingID=data['bookingID'],
            paymentMethod=data['paymentMethod'],
            transactionDate=data['transactionDate'],
            amount=data['amount']
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"message": "Payment added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# GET endpoint to fetch all payments
@payment_bp.route('/get_payments', methods=['GET'])
def get_payments():
    try:
        payments = Payment.query.all()
        payments_list = [
            {
                "paymentID": payment.paymentID,
                "bookingID": payment.bookingID,
                "paymentMethod": payment.paymentMethod,
                "transactionDate": payment.transactionDate,
                "amount": float(payment.amount)
            }
            for payment in payments
        ]
        return jsonify(payments_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
