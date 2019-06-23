/*1.a search future flights*/
-- if single trip
select *
from flight
where departure_time > now() and departure_airport = %s and arrival_airport = %s
and departure_date = %s

--if round trip, display the result of two queries
select *
from flight
where departure_time > now() and departure_airport = %s and arrival_airport = %s
and departure_date = %s

select *
from flight
where departure_time > now() and departure_airport = %s and arrival_airport = %s
and departure_date = %s
--this %s is the reture date. the departure_airport and arrival_airport are the opposite