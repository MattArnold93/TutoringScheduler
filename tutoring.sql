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
INSERT INTO users (firstname, lastname, email, password, accountStatus) VALUES ("We Meet", "Again", "Student@umw.edu", "Student", 3);
INSERT INTO users (firstname, lastname, email, password, accountStatus) VALUES ("Tutor", "Tutors", "Tutor@umw.edu", "Tutor", 2);
INSERT INTO users (firstname, lastname, email, password, accountStatus) VALUES ("Other", "Tutor", "Other@umw.edu", "Tutor", 2);

CREATE TABLE IF NOT EXISTS appointments
(
	numId INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (numId),
	/*datenum DATE(20) NOT NULL,
	appointmenttime TIME(30) NOT NULL,*/
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
	PRIMARY KEY (studentId),
	usremail varchar(30) NOT NULL,
	Monday varchar(100),
	Tuesday varchar(100),
	Wednesday varchar(100),
	Thursday varchar(100),
	Friday varchar(100),
	INDEX (studentId)
);

Insert INTO times (studentId, usremail, Monday, Tuesday, Wednesday, Thursday, Friday) VALUES (3, "Tutor@umw.edu", "10:00AM, 1:00PM", NULL, "4:00PM", NULL, NULL);
Insert INTO times (studentId, usremail, Monday, Tuesday, Wednesday, Thursday, Friday) VALUES (4, "Other@umw.edu", "10:00AM, 1:00PM", "6:00PM", "4:00PM", NULL, "5:00PM");
