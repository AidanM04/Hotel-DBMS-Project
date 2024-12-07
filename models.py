from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()  # Create the SQLAlchemy instance

# Example Guest table model
class Guest(db.Model):
    __tablename__ = 'Guest'
    guestID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return f"<Guest {self.first_name} {self.last_name}>"


class Room(db.Model):
    __tablename__ = 'Room'
    roomID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomType = db.Column(db.String(20), nullable=False, server_default='standard')
    roomNumber = db.Column(db.Integer, nullable=False)
    roomFloor = db.Column(db.Integer, nullable=False)
    pricePerNight = db.Column(db.Numeric(5, 2), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Room {self.roomNumber} on Floor {self.roomFloor}>"


class Booking(db.Model):
    __tablename__ = 'booking'

    bookingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomID = db.Column(db.Integer, db.ForeignKey('Room.roomID'), nullable=False)
    guestID = db.Column(db.Integer, db.ForeignKey('Guest.guestID'), nullable=False)
    checkInDate = db.Column(db.DateTime, nullable=False)
    checkOutDate = db.Column(db.DateTime, nullable=False)
    paymentStatus = db.Column(db.String(20), default='pending')

    def __repr__(self):
        return f"<Booking Room {self.roomID} Guest {self.guestID}>"

class Payment(db.Model):
    __tablename__ = 'Payment'

    paymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bookingID = db.Column(db.Integer, db.ForeignKey('booking.bookingID'), nullable=False)
    paymentMethod = db.Column(db.String(20), nullable=False)  # Example: 'credit card', 'debit card'
    transactionDate = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)

    # Optional backreference to the Booking model
    booking = db.relationship('Booking', backref='payments', lazy=True)

    def __repr__(self):
        return f"<Payment ID {self.paymentID} for Booking {self.bookingID}>"
    
class Service(db.Model):
    __tablename__ = 'Service'
    
    serviceID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serviceName = db.Column(db.String(100), nullable=False)
    servicePrice = db.Column(db.Numeric(5, 2), nullable=False)
    description = db.Column(db.String(500))
    
    def __repr__(self):
        return f"<Service {self.serviceName}>"

class Review(db.Model):
    __tablename__ = 'review'

    reviewID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guestID = db.Column(db.Integer, db.ForeignKey('guest.guestID'))
    bookingID = db.Column(db.Integer, db.ForeignKey('booking.bookingID'))
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    reviewDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Review ID {self.reviewID} for Booking {self.bookingID}>"
    
class BookingServices(db.Model):
    __tablename__ = 'BookingServices'
    
    bookingID = db.Column(db.Integer, db.ForeignKey('Booking.bookingID'), primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('Service.serviceID'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<BookingService Booking {self.bookingID} Service {self.serviceID}>"

