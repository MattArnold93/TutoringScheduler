DROP DATABASE TutoringScheduler;

CREATE DATABASE IF NOT EXISTS TutoringScheduler;
GRANT ALL PRIVILEGES ON TutoringScheduler.* to 'tUser'@'localhost'
identified by 'tPasswd';
USE TutoringScheduler;

CREATE TABLE IF NOT EXISTS users
(
	numId INT NOT NULL auto_increment,
	firstname varchar(50) NOT NULL,
	lastname varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	password varchar(228) NOT NULL,
	accountStatus int(1) NOT NULL,
	classes varchar(228),
  PRIMARY KEY (numId),
  INDEX (classes)
);

INSERT INTO users (firstname, lastname, email, password, accountStatus) VALUES ("Hi", "Testers", "Admin@umw.edu", "Admin", 1);
INSERT INTO users (firstname, lastname, email, password, accountStatus) VALUES ("We Meet", "Again", "Student@mail.umw.edu", "Student", 3);
INSERT INTO users (firstname, lastname, email, password, accountStatus, classes) VALUES ("Tutor", "Tutor", "Tutor@mail.umw.edu", "tutor", 2, "CPSC-110");
INSERT INTO users (firstname, lastname, email, password, accountStatus, classes) VALUES ("Toot", "Tutor", "Toot@mail.umw.edu", "tutor", 2, "CPSC-110,FREN-331");

CREATE TABLE IF NOT EXISTS appointments
(
	numId INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (numId),
    datenum int(20) NOT NULL,
	appointmenttime int(30) NOT NULL,
	class varchar(15) NOT NULL,
	studentId int(100) NOT NULL,
	tutorId int(100) NOT NULL,
  INDEX (tutorId)
);

CREATE TABLE IF NOT EXISTS classes
(
	numId INT NOT NULL auto_increment,
	PRIMARY KEY (numId),
	class varchar(15),
	subject varchar(15),
  INDEX (subject)
);

INSERT INTO classes (class, subject) VALUES ("CPSC-110", "CPSC");
INSERT INTO classes (class, subject) VALUES ("CPSC-220", "CPSC");
INSERT INTO classes (class, subject) VALUES ("SPAN-201", "SPAN");
INSERT INTO classes (class, subject) VALUES ("FREN-331", "FREN");

CREATE TABLE IF NOT EXISTS times
(
	studentId INT NOT NULL,
	classes varchar (400) NOT NULL,
	dayofweek varchar (10) NOT NULL,
	hourof varchar (10) NOT NULL,
	INDEX (studentId)
);

Insert INTO times (studentId, classes, dayofweek, hourof) VALUES (3, "CPSC-110", "Monday", "10:00AM");
Insert INTO times (studentId, classes, dayofweek, hourof) VALUES (4, "CPSC-110, FREN-331", "Tuesday", "1:00PM");
Insert INTO times (studentId, classes, dayofweek, hourof) VALUES (4, "CPSC-110, FREN-331", "Monday", "10:00AM");
