# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from datetime import date
from datetime import datetime
from dateutil import relativedelta
import random

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       port=8889,
                       user='root',
                       password='root',
                       db='Air-Ticket',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)



'''
on Eileen's server:
conn = pymysql.connect(host='localhost',
                       port=8889,
                       user='root',
                       password='root',
                       db='Air-Ticket',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

on Jenny's server
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='Air-Ticket',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
                       '''

# get the amount of seats

airline_name = 'China Southern'
flight_number = '100'
departure_date = '2019-08-11'
departure_time = '19:40:00'

cursor = conn.cursor()
query = '''select amount_of_seats
from flight natural join airplane
where airline_name = %s and flight_number = %s and departure_date = %s and departure_time = %s'''
cursor.execute(query, (airline_name, flight_number, departure_date, departure_time))
seat_data = cursor.fetchall()
# print(seat_data)
cursor.close()

# insert tickets for the flight
# generate ticket_id: airline_name abbr. + flight_number + fixed random number + serial order (last 3 digits)

to_add1 = ''
for i in airline_name:
    if i.isupper():
        to_add1 += i
random_num = random.randint(0,999)
to_add3 = str(random_num).zfill(3)
print(to_add1)
amount_of_seats = seat_data[0]['amount_of_seats']
cursor = conn.cursor()
for i in range(amount_of_seats):
    to_add2 = str(i).zfill(4)
    ticket_id = to_add1 + flight_number + to_add3 + to_add2
    print(ticket_id)
#     query = '''
#     insert into ticket (ticket_id, airline_name, flight_number, departure_date, departure_time)
#     values (%s, %s, %s, %s, %s)
#     '''
#     cursor.execute(query, (ticket_id, airline_name, flight_number, departure_date, departure_time))
#     conn.commit()
# cursor.close()
# print("insert finished")

