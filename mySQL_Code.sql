-- I use dBeaver for mySQL local projects

CREATE TABLE Guest (
    guestID INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(75) NOT NULL,
    phone CHAR(12) NOT NULL
);


CREATE TABLE Room (
    roomID INT AUTO_INCREMENT PRIMARY KEY,
    roomType VARCHAR(20) CHECK (roomType IN ('standard', 'deluxe')) DEFAULT 'standard',
    roomNumber INT NOT NULL,
    roomFloor INT NOT NULL,
    pricePerNight DECIMAL(5, 2) NOT NULL,
    description VARCHAR(500) NOT NULL
);


CREATE TABLE Booking (
    bookingID INT AUTO_INCREMENT PRIMARY KEY,
    roomID INT,
    guestID INT,
    checkInDate TIMESTAMP NOT NULL,
    checkOutDate TIMESTAMP NOT NULL,
    paymentStatus VARCHAR(20) CHECK (paymentStatus IN ('pending', 'paid', 'cancelled')) DEFAULT 'pending',
    FOREIGN KEY (roomID) REFERENCES Room(roomID),
    FOREIGN KEY (guestID) REFERENCES Guest(guestID)
);


CREATE TABLE Payment (
    paymentID INT AUTO_INCREMENT PRIMARY KEY,
    bookingID INT,
    paymentMethod VARCHAR(20) CHECK (paymentMethod IN ('credit card', 'debit card')),
    transactionDate TIMESTAMP,
    FOREIGN KEY (bookingID) REFERENCES Booking(bookingID)
);


CREATE TABLE Service (
    serviceID INT AUTO_INCREMENT PRIMARY KEY,
    serviceName VARCHAR(100) NOT NULL,
    servicePrice DECIMAL(5, 2) NOT NULL,
    description VARCHAR(500)
);


CREATE TABLE Review (
    reviewID INT AUTO_INCREMENT PRIMARY KEY,
    guestID INT,
    bookingID INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    comments TEXT,
    reviewDate DATE,
    FOREIGN KEY (guestID) REFERENCES Guest(guestID),
    FOREIGN KEY (bookingID) REFERENCES Booking(bookingID)
);


CREATE TABLE BookingServices (
    bookingID INT,
    serviceID INT,
    quantity INT,
    PRIMARY KEY (bookingID, serviceID),
    FOREIGN KEY (bookingID) REFERENCES Booking(bookingID),
    FOREIGN KEY (serviceID) REFERENCES Service(serviceID)
);
