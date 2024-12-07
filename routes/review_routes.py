from flask import Blueprint, request, jsonify
from models import db, Review

review_bp = Blueprint('review_bp', __name__)

# POST endpoint to add a review
@review_bp.route('/add_review', methods=['POST'])
def add_review():
    try:
        data = request.json
        new_review = Review(
            guestID=data['guestID'],
            bookingID=data['bookingID'],
            rating=data['rating'],
            comments=data.get('comments'),  # Optional
            reviewDate=data['reviewDate']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"message": "Review added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET endpoint to fetch all reviews
@review_bp.route('/get_reviews', methods=['GET'])
def get_reviews():
    try:
        reviews = Review.query.all()
        reviews_list = [
            {
                "reviewID": review.reviewID,
                "guestID": review.guestID,
                "bookingID": review.bookingID,
                "rating": review.rating,
                "comments": review.comments,
                "reviewDate": review.reviewDate.strftime('%Y-%m-%d')
            }
            for review in reviews
        ]
        return jsonify(reviews_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
