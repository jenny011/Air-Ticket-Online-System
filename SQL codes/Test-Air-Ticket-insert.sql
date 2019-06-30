INSERT INTO airline VALUES ('Air China');

create table purchase
	(ticket_id varchar(50),
	email varchar(50),
	purchase_date date,
	purchase_time time,
	sold_price float(2) not null,
	card_type varchar(50),
	card_number varchar(50),
	name_on_card varchar(50),
	expiraton_date date,
	primary key (ticket_id, email),
	foreign key (ticket_id) references ticket(ticket_id)
		on update cascade,
	foreign key (email) references customer(email)
		on update cascade
	);

INSERT INTO purchase VALUES ('1', 'testcustomer@nyu.edu', '2019-03-12', '11:55:55', '300', 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03');
INSERT INTO purchase VALUES ('2', 'user1@nyu.edu', '2019-03-11', '11:55:55', '300', 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03');
INSERT INTO purchase VALUES ('3', 'user2@nyu.edu', '2019-04-11', '11:55:55', '300', 'credit card', '1111-2222-3333-5555', 'User 2', '2023-03');
INSERT INTO purchase VALUES ('4', 'user1@nyu.edu', '2019-03-21', '11:55:55', '300', 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03');
INSERT INTO purchase VALUES ('5', 'testcustomer@nyu.edu', '2019-04-28', '11:55:55', '300', 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03');
INSERT INTO purchase VALUES ('6', 'user1@nyu.edu', '2019-03-05', '11:55:55', '350', 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03');
INSERT INTO purchase VALUES ('7', 'user3@nyu.edu', '2019-02-03', '11:55:55', '350', 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03');
INSERT INTO purchase VALUES ('8', 'user3@nyu.edu', '2018-10-03', '11:55:55', '300', 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03');
INSERT INTO purchase VALUES ('9', 'user3@nyu.edu', '2019-02-03', '11:55:55', '360', 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03');
INSERT INTO purchase VALUES ("11", 'user3@nyu.edu', '2018-10-23', '11:55:55', '300', 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03');
INSERT INTO purchase VALUES ('12', 'testcustomer@nyu.edu', '2019-04-05', '11:55:55', '500', 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03');
INSERT INTO purchase VALUES ('14', 'user3@nyu.edu', '2019-05-12', '11:55:55', '400', 'credit card', '1111-2222-3333-5555', 'User 3', '2023-03');
INSERT INTO purchase VALUES ('15', 'user1@nyu.edu', '2019-05-13', '11:55:55', '400', 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03');
INSERT INTO purchase VALUES ('16', 'user2@nyu.edu', '2019-04-19', '11:55:55', '400', 'credit card', '1111-2222-3333-5555', 'User 2', '2023-03');
INSERT INTO purchase VALUES ('17', 'user1@nyu.edu', '2019-03-11', '11:55:55', '300', 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03');
INSERT INTO purchase VALUES ('18', 'testcustomer@nyu.edu', '2019-04-25', '11:55:55', '300', 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03');
INSERT INTO purchase VALUES ('19', 'user1@nyu.edu', '2019-05-04', '11:55:55', '3000', 'credit card', '1111-2222-3333-5555', 'User 1', '2023-03');
INSERT INTO purchase VALUES ('20', 'testcustomer@nyu.edu', '2019-02-12', '11:55:55', '3000', 'credit card', '1111-2222-3333-4444', 'Test Customer 1', '2023-03');