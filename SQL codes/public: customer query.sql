

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



--query for ticket with price
creat view flight_price as
select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, 






