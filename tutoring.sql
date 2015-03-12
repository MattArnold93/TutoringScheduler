DROP DATABASE TutoringScheduler;

CREATE DATABASE IF NOT EXISTS TutoringScheduler;
GRANT ALL PRIVILEGES ON TutoringScheduler.* to 'tUser'@'localhost'
identified by 'tPasswd';
USE TutoringScheduler;

CREATE TABLE IF NOT EXISTS users
(
	numId INT NOT NULL auto_increment,
	primary key (numId),
	firstname varchar(50) NOT NULL,
	lastname varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	password varchar(1000) NOT NULL,
	accountStatus int(5) NOT NULL,
	classes varchar(400),
);
CREATE INDEX subject_type ON users (classes);

CREATE TABLE IF NOT EXISTS appointments
(
	numId INT not null auto_increment,
	primary key (numId),
	datenum DATE(20) NOT NULL,
	appointmenttime TIME(30) NOT NULL,
	class varchar(15) NOT NULL,
	studentId int(100) NOT NULL,
	tutorId int(100) NOT NULL
);
CREATE INDEX tutor_id ON appointments (tutorId);

CREATE TABLE IF NOT EXISTS classes
(
	numId INT not null auto_increment,
	primary key (numId),
	class varchar(15),
	subject varchar(15),
);
CREATE INDEX subject_name ON classes (subject);

