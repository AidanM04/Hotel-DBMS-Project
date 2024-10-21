# SQL Code Breakdown

This is a breakdown of the SQL code used for the project. There will be seven tables:
	- Guest
	- room
	- payment
	- review
	- booking
	- service
	- bookingService

 <u>Note:</u> If you are running this locally and using MySQL workspace, enter each table and run it manually. 
 Do not try and paste the whole code and try and run it all at once because you will get errors relating to foreign key relations. 
 In order for foreign key relations to exist, it needs a table first, so make each table first from the order listed above to create the database without any issues.

 # Guest Table

```
create table guest(
    guestID int primary key auto_increment,
    first_name varchar(40) not null,
    last_name varchar(50) not null,
    email varchar(75) not null,
    phone char(12) not null
);
```

Guest table has 5 attributes to it:
	- guestID: serves as the primary key, so each ID is unique and never null
	- first_name
	- last_name
	- email
	- phone

<u>Note:</u> Every guest should fill each attribute which is why all of them are set to not null

# Room table

```
create table room(
    roomID int primary key auto_increment,
    roomType enum("standard", "deluxe") default "standard",
    roomNumber int not null,
    roomFloor int not null,
    pricePerNight decimal(5, 2) not null,
    description varchar(500) not null
);
```

Room table has 6 attributes to it:
	- roomID: serves as the primary key
	- roomType
	- roomFloor
	- pricePerNight
	- description

 <u>Note:</u> These are all not null, and there are no foreign key attributes attached to this table. However, roomID will be used as a foreign key in other tables

# Payment Table

```
create table payment(
    paymentID int primary key auto_increment,
    bookingID int,
    paymentMethod enum("credit card", "debit card"),
    transactionDate Datetime
    CONSTRAINT fk_payment_booking FOREIGN KEY (bookingID) REFERENCES Booking(bookingID)
);
```

Payment table has 4 attributes attached to it:
	- paymentID: serves as the primary key
	- bookingID: foreign key, should reference the bookingID from the booking table
	- paymentMethod
	- transactionDate

 <u>Note:</u> This table could include extra attributes like card number, ccv, etc. The idea being is when a guest tries to book a room, they are taken to a form for payment and select the card first and then could prompt card number and all of that stuff. 
 For simplicity, a card type selection may be enough. If you try to include card details you may want to make sure it is formatted correctly, and if it is, then it will always be validated. This table does use a foreign key, bookingID. 

# Review Table

```
CREATE TABLE Review (
    reviewID INT AUTO_INCREMENT PRIMARY KEY,
    guestID INT,
    bookingID INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    comments TEXT,
    reviewDate DATE
);
```

Room table has 6 attriutes:
	- reviewID: serves as the primary key
	- guestID: foreign key
	- bookingID: foreign key
	- rating
	- comment
	- reviewDate

<u>Note:</u> There are two foreign keys in this table. A review should be connected to a guest and if they actually stayed in a hotel which is why the bookingID foreign key is here. 
The idea is the guest can visit the page and click on a review link and it takes them to a form to fill out a review.
 
# booking Table

```
create table booking(
    bookingID int primary key auto_increment,
    roomID int,
    guestID int,
    checkInDate datetime,
    checkOutTime datetime,
    paymentStatus enum('pending', 'paid', 'cancelled') default 'pending'
    CONSTRAINT fk_booking_room FOREIGN KEY (roomID) REFERENCES Room(roomID),
    CONSTRAINT fk_booking_guest FOREIGN KEY (guestID) REFERENCES Guest(guestID)
);
```

Booking table has 6 attributes
	- bookingID: primary key
	- roomID: foreign key
	- guestID: foreign key
	- checkInDate
	- checkOutDate
	- paymentStatus

<u>Note:</u> Tbh you can remove the paymentStatus if you want. If the guest fills out the payment form successfully then you could update the status, but I don't remember how I wanted to implement this exactly. 
Besides that, this table has two foreign keys. A room can be booked by a guest so it needs foreign keys from those tables to establish a successful booking.

# Service Table

```
CREATE TABLE service (
    serviceID INT AUTO_INCREMENT PRIMARY KEY,
    serviceName VARCHAR(100) NOT NULL,
    servicePrice DECIMAL(5, 2) NOT NULL,
    description VARCHAR(500)
);
```

Service table has 4 attributes:
	- serviceID: serves as the primary key
	- serviceName
	- servicePrice
	- description

<u>Note:</u> A guest can book a room yes, but a guest should probably be able to pick extra services if they way. The idea is to create yet another form that shows guest a selection of services they can pick from. 
That is the point of this table. It holds all the services offered by the hotel and holds the service details such as the name and price. For example, if the hotel offers breakfast, then that is stored in this table, 
and it would look something like this:
```
Insert into service("Breakfast", 15.99, "Chef prepares breakfast for you in the dining room");
```

# bookingService Table

```
CREATE TABLE BookingServices (
    bookingID INT,
    serviceID INT,
    quantity INT,     
    PRIMARY KEY (bookingID, serviceID),
    FOREIGN KEY (bookingID) REFERENCES Booking(bookingID),
    FOREIGN KEY (serviceID) REFERENCES Service(serviceID)
);
```

bookingService has 3 attributes:
	- bookingID: primary key, foreign key
	- serviceID: primary key, foreign key
	- quantity

 <u>Note:</u> Looking back at the old table, it made no sense to have a separate primary key as the goal of this table to track services that a booking has. 
 Basically, all connections between the services a booking has comes from this table, quantity would be the amount of times that service will be requested by the guest. 
 I got rid of the old primary key and decided that this table will have a composite key. The composite key consist of two foreign keys.
