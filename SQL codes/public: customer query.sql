

--if round trip, display the result of two queries
select *
from flight
where departure_time > now() and departure_airport = %s and arrival_airport = %s
and departure_date = %s

select *
from flight
where departure_time > now() and departure_airport = %s and arrival_airport = %s
and departure_date = %s
--this %s is the return date. the departure_airport and arrival_airport are the opposite



/*7. give ratings and comment on previous flights*/

--get unrated flights
select *
from (flight natural join ticket) join purchase using (ticket_id)
where timestamp(cast(arrival_date as datetime)+cast(arrival_time as time)) < now() and email = %s

--Assume: web returns the FLIGHT INFO on which the user wants to rate
--get user input: rating and comment
INSERT INTO `rates` (`email`, `airline_name`, `flight_number`, `departure_date`, `departure_time`, `rating`, `comments`) 
VALUES (%s, %s, %s, %s, %s, %s, %s);




-----------------------------------------------------
--todo: create view from price

--when the staff insert a flight, all the ticket should be inserted

/*
1. the staff insert a flight
you get the info:
airline_name = 
flight_number = 
departure_date = 
departure_time = 
base_price = 
id = 
*/

amount of seats = 
select amount_of_seats
from flight natural join airplane
where airline_name = %s and flight_number = %s and departure_date = %s and departure_time = %s
and base_price = %s and id = %s

--automatically generate ticket id?

for i in range(amount_of_seats):
    ticket_id = flight_number + str(i)






















/*4. view my flights*/
--after login: how can i get the customer_id?
select *
from (flight natural join ticket) join purchase using (ticket_id)
where email = /*the customer email you need to get*/
--ignore for now, to let the user specify range of dates/destination/source

/*5. search for flights*/
--the same as /*1*/

--a query for calculating the price
--possible conflict

creat view flight_price as
select airline_name, flight_number, departure_date, departure_time, 

--having price in the ticket table recommended
/*
create view price as
select CASE WHEN num_sold < 0.7 * 
    (select amount_of_seats 
    from (ticket natural join flight) join airplane using (airline_name, id)
    where where airline_name = %s and flight_number = %s and departure_date = %s and departure_time = %s)
    THEN base_price
    ELSE base_price * 1.2
    end as price
from
(count(ticket_id)) as num_sold
from ticket
where airline_name = %s and flight_number = %s and departure_date = %s and departure_time = %s 
and ticket_id not in (select ticket_id from purchase)
*/


/*6. purchase tickets*/
--ticket_id, get the first_ticket id that is not taken---how?

create table temporal_ticket(
    email varchar(50) not null,
    ticket_id varchar(50) not null,
    airline_name varchar(50),
	flight_number varchar(20) not null,
	departure_date date not null,
	departure_time time not null,
    click_date date,
    click_time time,
    price float(2) not null
    primary key (email, airline_name, flight_number, departure_date, departure_time)
    foreign key (email) references customer(email),
    foreign key (airline_name, flight_number, departure_date, departure_time) references flight(airline_name, flight_number, departure_date, departure_time)
		on update cascade
	);
--the ticket is kept for 10 mins. 

--(1) choose the ticket to buy
--get the ticket
--in what form is the ticket id? how is ticket_id created? [assume ticket exists before it gets sold]
insert into temporal_ticket (email, ticket_id, airline_name, flight_number, departure_date, departure_time, click_date, click_time)
values(/*get email*/, /*get ticket id*/, /*four spaces for flight info*/, cast(now() as date), cast(now() as time));

--(2) input payment info (and the ticket purchasing is finished)
--you need to calculate price
insert into purchase(ticket_id, email, purchase_date, purchase_time, sold_price, card_type, card_number, name_on_card, expiration_date)
values 









