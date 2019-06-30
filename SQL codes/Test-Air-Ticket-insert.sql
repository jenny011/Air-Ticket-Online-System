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

INSERT INTO purchase VALUES ('1', 'testcustomer@nyu.edu', '2019-03-12', '11:55:55', '300', 'credit card', '111-222-333-444', 'Test Customer 1', '2026-01-01');

INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
INSERT INTO purchase VALUES ('a00000001', 'js123@outlook.com', '2019-05-12', '00:10:10', '4000', 'credit card', '600080009000111', 'John Smith', '2026-01-01');
