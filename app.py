from flask import Flask
from flask_cors import  CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, Guest, Room, Booking, Payment, Service, Review, BookingServices
from routes.booking_routes import booking_bp
from routes.guest_routes import guest_bp
from routes.payment_routes import payment_bp
from routes.room_routes import room_bp
from routes.service_routes import service_bp  
from routes.review_routes import review_bp
from routes.booking_service_routes import booking_service_bp
app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Niceroad%4020@localhost/hotel_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with Flask
db.init_app(app)



# Register blueprints
app.register_blueprint(room_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(service_bp)
app.register_blueprint(review_bp)
app.register_blueprint(booking_service_bp)
# Optional: Test route to confirm app is running
@app.route('/')
def home():
    return "Welcome to the Hotel Management System!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

