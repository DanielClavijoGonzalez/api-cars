CREATE SCHEMA s1tester_api_cars;

CREATE TABLE cars (
	id int primary key not null auto_increment,
	name varchar(15) not null,
    brand varchar(30) not null,
    image varchar(256) not null,
    createDate datetime default now()
);