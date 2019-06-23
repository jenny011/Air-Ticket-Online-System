

/*4.view flights*/

--get the airline_name
--1). the default (next 30 days), in the staff homepage
select *
from flight
where airline_name = %s 
and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= CURTIME() + INTERVAL 30 DAY

--2). search based on range of dates
select *
from flight
where airline_name = %s 
and departure_date between %s and %s
--to return: redirect to customer homepage or go to a new page?

--3). search based on source/destination airports/city
--so far only allow users to input airport.
--could improve later
select *
from flight
where airline_name = %s 
and departure_airport = s% and arrival_airport = %s
--to return: redirect to customer homepage or go to a new page?


/*5.create new flights*/
--what do you mean "authorized user"? staff not customer? or only a portion of staff?
--how to manage the flight-status default? it is an input value or not?
INSERT INTO flight (airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, base_price, status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)


/*6. change the status of flights*/

--ideally, the user could choose the flight to update
--the user could choose the flight status to change into

--get the (airline_name, fligh_number, departure_date, departure_time)
update flight
set status = %s
where (airline_name, fligh_number, departure_date, departure_time) = (%s, %s, %s, %s)


/*7. add airplane in the system*/
INSERT INTO airplane (airline_name, id, amount_of_seats)
VALUES (%s, %s, %s)


/*8. add airport in the system*/
insert into airport (airport_name, city)
values (%s, %s)


/*9. view flight ratings*/
--aveage ratings

