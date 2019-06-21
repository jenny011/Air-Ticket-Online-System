/*4.view flights*/
--the default
--get the airline_name
select *
from flight
where airline_name = %s and timestamp(departure_date,departure_time) between now() and ;