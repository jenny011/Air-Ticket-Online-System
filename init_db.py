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

@app.route('/')
def public():
    return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/register_staff')
def register_staff():
    return render_template('register-staff.html')

@app.route('/register_customer')
def register_customer():
    return render_template('register-customer.html')


@app.route('/login')
def login():
	return render_template('login.html')
#login page, choose staff or customer
@app.route('/login_staff')
def login_staff():
    return render_template('login-staff.html')

@app.route('/login_customer')
def login_customer():
    return render_template('login-customer.html')


#==========================================================#

#----------------Authenticates the register----------------#
@app.route("/registerAuth", methods=['GET', 'POST'])
def registerAuth():
    usertype = request.form['usertype']
    if usertype == 'Staff':
        return redirect(url_for('register_staff'))
    elif usertype == 'Customer':
        return redirect(url_for('register_customer'))

@app.route("/registerStaffAuth", methods=['GET', 'POST'])
def registerStaffAuth():
    # grabs information from the forms
    username = request.form['username']
    airline_name = request.form['airline-name']
    password = request.form['password']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    DOB = request.form['DOB']
    # phone_number = request.form['phone-number']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM airline_staff WHERE user_name = %s'
    cursor.execute(query, (username))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register-staff.html', error=error)
    else:
        ins = 'INSERT INTO airline_staff VALUES(%s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (username, airline_name, password,
                             first_name, last_name, DOB))
        conn.commit()
        cursor.close()
        #todo: redirect to staff login page?
        return render_template('login-staff.html')

@app.route("/registerCustomerAuth", methods=['GET', 'POST'])
def registerCustomerAuth():
    # grabs information from the forms
    email = request.form['username']
    password = request.form['password']
    name = request.form['name']
    DOB = request.form['DOB']
    phone_number = request.form['phone-number']
    building_number = request.form['building-number']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    passport_number = request.form['passport-number']
    passport_expiration = request.form['passport-expiration']
    passport_country = request.form['passport-country']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM customer WHERE email = %s'
    cursor.execute(query, (email))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error=error)
    else:
        ins = 'INSERT INTO customer VALUES' \
              '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (email, name, password,
                             building_number, street, city, state,
                             phone_number, passport_number, passport_expiration,
                             passport_country, DOB))
        conn.commit()
        cursor.close()
        #todo: redirect to customer login page?
        return render_template('login-customer.html')


#-----------------Authenticates the login------------------#
@app.route("/loginAuth", methods=['GET', 'POST'])
def loginAuth():
    usertype = request.form['usertype']
    if usertype == 'Staff':
        return redirect(url_for('login_staff'))
    elif usertype == 'Customer':
        return redirect(url_for('login_customer'))

@app.route("/loginStaffAuth", methods=['GET', 'POST'])
def loginStaffAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM airline_staff WHERE user_name = %s and password = %s'
    cursor.execute(query, (username, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        session['usertype'] = "staff"
        session['airline'] = data['airline_name']
        return redirect(url_for('staff_home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login-staff.html', error=error)  # send the error msg to html
    # communicate between python and html

@app.route('/loginCustomerAuth', methods=['GET', 'POST'])
def loginCustomerAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM customer WHERE email = %s and password = %s'
    cursor.execute(query, (username, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in dictionary
        session['username'] = username
        session['usertype'] = "customer"
        return redirect(url_for('customer_home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login-customer.html', error=error)  # send the error msg to html



#============== public_index =====================#

# public search
@app.route('/searchPublic', methods=['GET', 'POST'])
def searchPublic():
    #get search info from page and execute in sql db
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        # print("data in search public", data1)
        cursor.close()
        return render_template('search-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query1 = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query1, (source, destination, departure_date))
        data1 = cursor.fetchall()
        # conn.commit()
        cursor.close()

        cursor = conn.cursor()
        query2 = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query2, (destination, source, return_date))
        # execution not successful
        data2 = cursor.fetchall()
        print("return flight info", data2)
        cursor.close()
        return render_template('search-round.html', source=source, destination=destination, departure_date=departure_date,
                               return_date=return_date, departure_flights=data1, return_flights=data2)

@app.route("/searchPublicOneWay", methods=['GET', 'POST'])
def searchPublicOneWay():
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()

        cursor.close()
        return render_template('search-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query = 'select * from flight_price ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        #cursor.close()

        #cursor = conn.cursor()
        query = 'select * from flight_price ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (destination, source, return_date))
        data2 = cursor.fetchall()
        cursor.close()

        return render_template('search-round.html', source=source, destination=destination,
                               departure_date=departure_date, return_date=return_date, departure_flights=data1, return_flights=data2)

@app.route("/searchPublicRound", methods=['GET', 'POST'])
def searchPublicRound():
        source = request.form['source']
        destination = request.form['destination']
        triptype = request.form['triptype']
        departure_date = request.form['departure-date']

        if triptype == "one-way":
            cursor = conn.cursor()
            query = '''select * from flight_price natural join flight_seats_sold
                    where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                    and departure_airport = %s and arrival_airport = %s and departure_date = %s
                    and amount_of_seats > tickets_sold'''
            cursor.execute(query, (source, destination,departure_date))
            data1 = cursor.fetchall()
            cursor.close()
            return render_template('search-one.html', source=source, destination=destination, departure_date = departure_date, flights=data1)

        elif triptype == "round":
            return_date = request.form['return-date']
            cursor = conn.cursor()
            query = '''select * from flight_price natural join flight_seats_sold
                    where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                    and departure_airport = %s and arrival_airport = %s and departure_date = %s
                    and amount_of_seats > tickets_sold'''
            cursor.execute(query, (source, destination, departure_date))
            data1 = cursor.fetchall()
            cursor.close()

            cursor = conn.cursor()
            query = '''select * from flight_price natural join flight_seats_sold
                    where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                    and departure_airport = %s and arrival_airport = %s and departure_date = %s
                    and amount_of_seats > tickets_sold'''
            cursor.execute(query, (destination, source, return_date))
            data2 = cursor.fetchall()
            cursor.close()
            return render_template('search-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, departure_flights=data1, return_flights=data2)



# ------------- public check ------------------
@app.route("/checkIndex", methods=['GET', 'POST'])
def checkIndex():
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    datetype = request.form['datetype']
    date = request.form['date']

    if datetype == "departure_date":
        cursor = conn.cursor()
        query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight ' \
                'where airline_name = %s and flight_number = %s and departure_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date,datetype=datetype)

    elif datetype == "arrival_date":
        cursor = conn.cursor()
        query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight ' \
                'where airline_name = %s and flight_number = %s and arrival_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date,datetype=datetype)

@app.route("/checkPublic", methods=['GET', 'POST'])
def checkPublic():
    airline_name = request.form['airline_name']
    flight_number = request.form['flight_number']
    datetype = request.form['datetype']
    date = request.form['date']

    if datetype == "departure_date":
        cursor = conn.cursor()
        query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight where airline_name = %s and flight_number = %s and departure_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date,datetype=datetype)

    elif datetype == "arrival_date":
        cursor = conn.cursor()
        query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight where airline_name = %s and flight_number = %s and arrival_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date,datetype=datetype)


#==============================================================================
#==============================================================================
# ================ Customer Use Cases ===================

#-------------------------------customer home----------------------------------
@app.route('/customer_home')
def customer_home():
    username = session['username']
    today = date.today()
    to_date = today
    from_date = date(today.year-1, today.month, today.day)

    # view
    cursor = conn.cursor()
    query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
    from (flight natural join ticket) join purchase using (ticket_id)
    where email = %s and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
    cursor.execute(query, (username,today))
    data1 = cursor.fetchall()
    cursor.close()
    #rate
    cursor = conn.cursor()
    query = 'select airline_name, flight_number, departure_date, departure_time, departure_airport, arrival_airport ' \
            'from (flight natural join ticket) join purchase using (ticket_id)' \
            'where timestamp(cast(arrival_date as datetime)+cast(arrival_time as time)) < now() ' \
            'and email = %s and ' \
            'ticket_id not in ' \
            '(select ticket_id ' \
            'from (flight natural join ticket) join purchase using (ticket_id) join rates using (email, airline_name, flight_number, departure_date, departure_time))'
    cursor.execute(query, (username))
    data2 = cursor.fetchall()
    cursor.close()

    #Track-total
    cursor = conn.cursor()
    query = '''select sum(sold_price) from purchase where email = %s
    and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) >= %s
    and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) < %s'''
    cursor.execute(query, (username, from_date, to_date))
    total_spending = cursor.fetchall()
    if total_spending[0]['sum(sold_price)']==None:
        total_spending[0]['sum(sold_price)']=0
    cursor.close()
    #Track-monthly
    cursor = conn.cursor()
    monthly_spending = []
    months=[]
    date1 = datetime.strptime(str(from_date), '%Y-%m-%d')
    date2 = datetime.strptime(str(to_date), '%Y-%m-%d')
    # r = relativedelta.relativedelta(date2, date1)
    # month_number = r.months + r.years*12
    month_number = (date2.year-date1.year)*12 + date2.month - date1.month
    if from_date.day != 1:
        month_number += 1
    for i in range(month_number):
        query = '''select sum(sold_price) from purchase where email = %s
        and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) >= %s
        and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) < %s'''
        if from_date.month+i <= 12:
            from_d_year = from_date.year
            from_d_month = from_date.month+i
        else:
            from_d_year = from_date.year+1
            from_d_month = from_date.month+i-12
        if from_date.month+i+1 <= 12:
            to_d_year = from_date.year
            to_d_month = from_date.month+i+1
        else:
            to_d_year = from_date.year+1
            to_d_month = from_date.month+i-11
        if i == 0:
            from_d_day = from_date.day
        else:
            from_d_day = 1
        if i == month_number-1:
            to_d_month = to_date.month
            to_d_day = to_date.day
        else:
            to_d_day = 1
        from_d = date(from_d_year,from_d_month,from_d_day)
        to_d = date(to_d_year,to_d_month,to_d_day)
        cursor.execute(query, (username, from_d, to_d))
        monthly=cursor.fetchall()
        if monthly[0]['sum(sold_price)']==None:
            monthly[0]['sum(sold_price)']=0
        months.append(str(from_d_year)+"-"+str(from_d_month))
        monthly_spending.append(monthly)
    cursor.close()

    return render_template('customer-home.html', flights=data1, unrated=data2, total=total_spending[0]['sum(sold_price)'], monthly_spending=monthly_spending, from_date=to_date, from_date_track=from_date,to_date_track=to_date, display_number = 6, months = months)

#------------------------------------------------------------------------------
#---------!customer! search flights-------------
#old search query
# query = 'select * from flight_price ' \
#         'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
#         'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
@app.route('/search', methods=['GET', 'POST'])
def search():
    #display the search result
    usertype = session['usertype']
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        # return render_template('search-customer-one.html', source=source, flights=data1)
        return render_template('search-customer-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (destination, source, return_date))
        data2 = cursor.fetchall()
        cursor.close()
        return render_template('search-customer-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, departure_flights=data1, return_flights=data2)

@app.route('/searchCustomerOneWay', methods=['GET', 'POST'])
def searchCustomerOneWay():
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-customer-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (destination, source, return_date))
        data2 = cursor.fetchall()
        cursor.close()
        return render_template('search-customer-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, departure_flights=data1, return_flights=data2)

@app.route("/searchCustomerRound", methods=['GET', 'POST'])
def searchCustomerRound():
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination,departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-customer-one.html', source=source, destination=destination, departure_date = departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()

        cursor = conn.cursor()
        query = '''select * from flight_price natural join flight_seats_sold
                where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now()
                and departure_airport = %s and arrival_airport = %s and departure_date = %s
                and amount_of_seats > tickets_sold'''
        cursor.execute(query, (destination, source, return_date))
        data2 = cursor.fetchall()
        cursor.close()
        print(data1,data2)
        return render_template('search-customer-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, departure_flights=data1, return_flights=data2)


#---------!customer! purchase flights-------------
@app.route("/purchaseCustomerOneWay", methods=['POST'])
def purchaseCustomerOneWay():
    airline_name = request.form['airline-name']
    flight_number = request.form['flight-number']
    departure_date = request.form['departure-date']
    departure_time = request.form['departure-time']
    arrival_date = request.form['arrival-date']
    arrival_time = request.form['arrival-time']
    source = request.form['source']
    destination = request.form['destination']
    price = request.form['price']
    # get ticket info
    cursor = conn.cursor()
    query = '''select ticket_id
            from ticket
            where airline_name = %s and flight_number = %s and departure_date = %s and departure_time = %s
            and ticket_id not in (select ticket_id from purchase)'''
    cursor.execute(query, (airline_name, flight_number, departure_date, departure_time))
    ticket_id = cursor.fetchone()
    print(ticket_id)
    cursor.close()
    # store flight info in session
    flight_info1 = {"airline_name":airline_name, "flight_number":flight_number, "departure_date":departure_date, "departure_time": departure_time,
                    "arrival_date": arrival_date, "arrival_time": arrival_time, "source": source, "destination": destination,
                    "price": price, "ticket_id": ticket_id["ticket_id"]}
    session['flight_info1'] = flight_info1
    return render_template("purchase-customer.html", flights=[flight_info1], total=flight_info1["price"])


@app.route("/purchaseCustomerRound", methods=['GET', 'POST'])
def purchaseCustomerRound():
    pass


@app.route("/purchase_customer", methods=['GET', 'POST'])
def purchase_Customer():
    render_template("purchase-customer.html")


@app.route("/payCustomer", methods=['GET', 'POST'])
def payCustomer():
    username = session['username']
    flight_info1 = session['flight_info1']
    purchase_date = date.today()
    purchase_time = datetime.now().time()
    # print(purchase_time)
    # not sure if purchase_time is in correct format
    card_type = request.form["cardtype"]
    card_number = request.form['card-number']
    name_on_card = request.form['name-on-card']
    card_expiration = request.form['card-expiration']
    cursor = conn.cursor()
    ins = '''insert into purchase
    (ticket_id, email, purchase_date, purchase_time, sold_price, card_type, card_number, name_on_card, expiraton_date)
    values (%s, %s, cast(now() as date), cast(now() as time), %s, %s, %s, %s, %s)
    '''
    cursor.execute(ins, (flight_info1["ticket_id"], username, flight_info1["price"],
                           card_type, card_number, name_on_card, card_expiration))
    conn.commit()
    cursor.close()
    return redirect(url_for('customer_home'))

#------------------------------------------------------------------------------
#------------!customer! rate my flights-------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PROBLEM
@app.route("/rate", methods=['POST'])
def rate():
    print(request.method)
    airline = request.form['airline']
    number = request.form['number']
    date = request.form['date']
    time = request.form['time']
    source = request.form['source']
    destination = request.form['destination']
    return render_template('rate-customer.html',airline_name=airline, flight_number=number, departure_date=date, departure_time=time, source=source, destination=destination)

@app.route("/rateCustomer", methods=['GET', 'POST'])
def rateCustomer():
    username = session['username']
    airline_name = request.form['airline-name']
    flight_number = request.form['flight-number']
    departure_date = request.form['departure-date']
    departure_time = request.form['departure-time']
    rate = request.form['rate']
    comment = request.form['comment']

    cursor = conn.cursor()
    ins = 'INSERT INTO rates VALUES' \
          '(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(ins, (username, airline_name, flight_number,
                         departure_date, departure_time, rate, comment))
    conn.commit()
    cursor.close()
    return redirect(url_for('customer_home'))


#------------------------------------------------------------------------------
#------------!customer! view my flights-----------
@app.route('/view', methods=['GET', 'POST'])
def view():
    username = session['username']
    source = request.form['source']
    destination = request.form['destination']
    from_date = request.form['from-date']
    to_date = request.form['to-date']

    if from_date == "":
        from_date = date.today()
    if to_date == "":
        if source == "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and arrival_airport = %s
            and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, destination, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and departure_airport = %s
            and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, source, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and departure_airport = %s and arrival_airport = %s
            and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, source, destination, from_date))
            data1 = cursor.fetchall()
            cursor.close()
    else:
        if source == "" and destination == "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_date between %s and %s'
            cursor.execute(query, (username, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "" and destination != "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and arrival_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, destination, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination == "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination != "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s and arrival_airport = %s ' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, destination, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
    return render_template('view-customer.html', from_date=from_date, to_date=to_date,
                           source=source, destination=destination, flights=data1)

@app.route("/viewCustomer", methods=['GET', 'POST'])
def viewCustomer():
    username = session['username']
    source = request.form['source']
    destination = request.form['destination']
    from_date = request.form['from-date']
    to_date = request.form['to-date']

    if from_date == "":
        from_date = date.today()
    if to_date == "":
        if source == "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and arrival_airport = %s
            and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, destination, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and departure_airport = %s
            and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, source, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from (flight natural join ticket) join purchase using (ticket_id)
            where email = %s and departure_airport = %s and arrival_airport = %s
            and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s'''
            cursor.execute(query, (username, source, destination, from_date))
            data1 = cursor.fetchall()
            cursor.close()
    else:
        if source == "" and destination == "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_date between %s and %s'
            cursor.execute(query, (username, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "" and destination != "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and arrival_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, destination, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination == "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination != "":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s and arrival_airport = %s ' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, destination, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
    return render_template('view-customer.html', from_date=from_date, to_date=to_date,
                           source=source, destination=destination, flights=data1)


#------------------------------------------------------------------------------
#------------!customer! track my spending-----------
@app.route("/track", methods=['GET', 'POST'])
def track():
    # when the user specify from-date and to-date
    username = session['username']
    from_date_track = request.form['from-date']
    to_date_track = request.form['to-date']
    cursor = conn.cursor()
    query = '''select sum(sold_price) from purchase where email = %s
    and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) >= %s
    and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) < %s'''
    cursor.execute(query, (username, from_date_track, to_date_track))
    total_spending = cursor.fetchall()
    if total_spending[0]['sum(sold_price)']==None:
        total_spending[0]['sum(sold_price)']=0
    cursor.close()
    #Track-monthly
    cursor = conn.cursor()
    monthly_spending = []
    months=[]
    date1 = datetime.strptime(from_date_track, '%Y-%m-%d')
    date2 = datetime.strptime(to_date_track, '%Y-%m-%d')
    # r = relativedelta.relativedelta(date2, date1)
    # month_number = r.months + r.years*12
    year_number = date2.year-date1.year+1
    for i in range(year_number):
        if i == 0 and year_number > 1:
            month_number = 13 - date1.month
            init_month = date1.month
        elif i == year_number - 1 and year_number > 1:
            month_number = date2.month
            init_month = 1
        elif year_number > 1:
            month_number = 12
            init_month = 1
        else:
            month_number = date2.month - date1.month + 1
            init_month = date1.month
        for j in range(month_number):
            query = '''select sum(sold_price) from purchase where email = %s
            and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) >= %s
            and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) < %s'''
            if init_month+j <= 12:
                from_d_year = date1.year+i
                from_d_month = init_month+j
            else:
                from_d_year = date1.year+1+i
                from_d_month = init_month+j-12
            if init_month+j+1 <= 12:
                to_d_year = date1.year+i
                to_d_month = init_month+j+1
            else:
                to_d_year = date1.year+1+i
                to_d_month = init_month+j-11
            if j == 0 and i == 0:
                from_d_day = date1.day
            else:
                from_d_day = 1
            if j == month_number -1 and i == year_number-1:
                to_d_month = date2.month
                to_d_day = date2.day
            else:
                to_d_day = 1
            from_d = date(from_d_year,from_d_month,from_d_day)
            to_d = date(to_d_year,to_d_month,to_d_day)
            # print(from_d,to_d)
            cursor.execute(query, (username, from_d, to_d))
            monthly=cursor.fetchall()
            if monthly[0]['sum(sold_price)']==None:
                monthly[0]['sum(sold_price)']=0
            months.append(str(from_d_year)+"-"+str(from_d_month))
            monthly_spending.append(monthly)
    month_number = (date2.year-date1.year)*12 + date2.month - date1.month
    if date2.day != 1:
        month_number += 1
    cursor.close()
    # print(monthly_spending)
    return render_template('track-customer.html', total=total_spending[0]['sum(sold_price)'], monthly_spending=monthly_spending, from_date_track=from_date_track, to_date_track=to_date_track, month_numnber=month_number, display_number = month_number, months = months)


#--------------------------------------------------------------------------------
#track-customer page
@app.route("/trackCustomer", methods=['GET', 'POST'])
def trackCustomer():
    # when the user specify from-date and to-date
    username = session['username']
    from_date_track = request.form['from-date']
    to_date_track = request.form['to-date']
    cursor = conn.cursor()
    query = '''select sum(sold_price) from purchase where email = %s
    and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) >= %s
    and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) < %s'''
    cursor.execute(query, (username, from_date_track, to_date_track))
    total_spending = cursor.fetchall()
    if total_spending[0]['sum(sold_price)']==None:
        total_spending[0]['sum(sold_price)']=0
    cursor.close()
    #Track-monthly
    cursor = conn.cursor()
    monthly_spending = []
    months=[]
    date1 = datetime.strptime(from_date_track, '%Y-%m-%d')
    date2 = datetime.strptime(to_date_track, '%Y-%m-%d')
    # r = relativedelta.relativedelta(date2, date1)
    # month_number = r.months + r.years*12
    year_number = date2.year-date1.year+1
    for i in range(year_number):
        if i == 0 and year_number > 1:
            month_number = 13 - date1.month
            init_month = date1.month
        elif i == year_number - 1 and year_number > 1:
            month_number = date2.month
            init_month = 1
        elif year_number > 1:
            month_number = 12
            init_month = 1
        else:
            month_number = date2.month - date1.month + 1
            init_month = date1.month
        for j in range(month_number):
            query = '''select sum(sold_price) from purchase where email = %s
            and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) >= %s
            and timestamp(cast(purchase_date as datetime)+cast(purchase_time as time)) < %s'''
            if init_month+j <= 12:
                from_d_year = date1.year+i
                from_d_month = init_month+j
            else:
                from_d_year = date1.year+1+i
                from_d_month = init_month+j-12
            if init_month+j+1 <= 12:
                to_d_year = date1.year+i
                to_d_month = init_month+j+1
            else:
                to_d_year = date1.year+1+i
                to_d_month = init_month+j-11
            if j == 0 and i == 0:
                from_d_day = date1.day
            else:
                from_d_day = 1
            if j == month_number -1 and i == year_number-1:
                to_d_month = date2.month
                to_d_day = date2.day
            else:
                to_d_day = 1
            from_d = date(from_d_year,from_d_month,from_d_day)
            to_d = date(to_d_year,to_d_month,to_d_day)
            # print(from_d,to_d)
            cursor.execute(query, (username, from_d, to_d))
            monthly=cursor.fetchall()
            if monthly[0]['sum(sold_price)']==None:
                monthly[0]['sum(sold_price)']=0
            months.append(str(from_d_year)+"-"+str(from_d_month))
            monthly_spending.append(monthly)
    month_number = (date2.year-date1.year)*12 + date2.month - date1.month
    if date2.day != 1:
        month_number += 1
    cursor.close()
    # print(monthly_spending)
    return render_template('track-customer.html', total=total_spending[0]['sum(sold_price)'], monthly_spending=monthly_spending, from_date_track=from_date_track, to_date_track=to_date_track, month_numnber=month_number, display_number = month_number, months = months)



#logout is the same for customer and staff
@app.route('/logout',methods=['GET','POST'])
def logout():
    usertype = session['usertype']
    if usertype == "customer" and session['flight_info1'] is not None:
        session.pop('flight_info1')
    if usertype == "staff":
        session.pop('airline')
    session.pop('usertype')
    session.pop('username')
    return render_template("logout.html")



#==============================================================================
#==============================================================================
#===============Airline Staff use case============
@app.route('/staff_home',methods=['GET','POST'])
def staff_home():
    username = session['username']
    airline = session['airline']
    cursor = conn.cursor();
    query = 'SELECT * FROM flight WHERE airline_name = %s ORDER BY ts DESC'
    cursor.execute(query, (airline))
    data1 = cursor.fetchall()
    cursor.close()
    return render_template('staff-home.html', username=username, flights=data1)

####!!!!!next 30 days???????????????
#--------------view flights TODO????????all customers-------------
@app.route('/viewFlights',methods=['GET','POST'])
def viewFlights():
    airline = session['airline']
    source = request.form['source']
    destination = request.form['destination']
    from_date = request.form['from-date']
    to_date = request.form['to-date']

    if from_date == "":
        from_date = date.today()
    if to_date == "":
        if source == "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, status
            from flight
            where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s
            and airline_name = %s'''
            cursor.execute(query, (from_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time,
                departure_airport, arrival_airport, status
                from flight
                where arrival_airport = %s
                and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s
                and airline_name = %s'''
            cursor.execute(query, (destination, from_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time,
                departure_airport, arrival_airport, status
                from flight
                where departure_airport = %s
                and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s
                and airline_name = %s'''
            cursor.execute(query, (source, from_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time, arrival_date, arrival_time,
                departure_airport, arrival_airport, status
                from flight
                where departure_airport = %s and arrival_airport = %s
                and timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s
                and airline_name = %s'''
            cursor.execute(query, (source, destination, from_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
    else:
        if source == "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time,
                    arrival_date, arrival_time, departure_airport, arrival_airport, status
                    from flight
                    where departure_date between %s and %s
                    and airline_name = %s'''
            cursor.execute(query, (from_date, to_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time,
                    arrival_date, arrival_time, departure_airport, arrival_airport, status
                    from flight
                    where arrival_airport = %s
                    and departure_date between %s and %s
                    and airline_name = %s'''
            cursor.execute(query, (destination, from_date, to_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination == "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time,
                    arrival_date, arrival_time, departure_airport, arrival_airport, status
                    from flight
                    where departure_airport = %s
                    and departure_date between %s and %s
                    and airline_name = %s'''
            cursor.execute(query, (source, from_date, to_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "" and destination != "":
            cursor = conn.cursor()
            query = '''select airline_name, flight_number, departure_date, departure_time,
                    arrival_date, arrival_time, departure_airport, arrival_airport, status
                    from flight
                    where departure_airport = %s and arrival_airport = %s
                    and departure_date between %s and %s
                    and airline_name = %s'''
            cursor.execute(query, (source, destination, from_date, to_date, airline))
            data1 = cursor.fetchall()
            cursor.close()
    return render_template('view-flights-staff.html', from_date=from_date, to_date=to_date,
                           source=source, destination=destination, flights=data1)


#--------------change flight status TODO--------------


#--------------create flights TOTEST------------------
@app.route('/createFlight',methods=['GET','POST'])
def createFlight():
    username = session['username']
    usertype = session['usertype']
    if usertype == "staff":
        airline = session['airline']
        flight_number = request.form['flight-number']
        departure_date = request.form['departure-date']
        departure_time = request.form['departure-time']
        arrival_date = request.form['arrival-date']
        arrival_time = request.form['arrival-time']
        departure_airport = request.form['departure-airport']
        arrival_airport = request.form['departure-airport']
        base_price = request.form['base-price']
        airplane_id = request.form['airplane-id']

        cursor = conn.cursor();
        query = '''select * from flight
          where airline_name=%s and flight_number=%s and departure_date=%s and deparutre_time=%s'''
        cursor.execute(query, (airline, flight_number, departure_date, departure_time))
        data = cursor.fetchall()
        cursor.close()

        exist_flight = None
        if(data):
            return redirect(url_for('/staff_home'),exist_flight="This flight already exists.")
        else:
            cursor = conn.cursor();
            ins = 'INSERT INTO flight VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(ins, (airline, flight_number, departure_date, departure_time, arrival_date, arrival_time, departure_airport, arrival_airport, base_price, status, airplane_id))
            conn.commit()
            cursor.close()

            #add ticket
            cursor = conn.cursor();
            query = '''select amount_of_seats from flight natural join airplane
                where airline_name = %s and flight_number = %s and departure_date = %s and departure_time = %s'''
            cursor.execute(query, (airline, flight_number, departure_date, departure_time))
            seats = cursor.fetchall()
            cursor.close()
            seats = seats['amount_of_seats']

            cursor = conn.cursor();
            query = '''select max(ticket_id) from ticket
              where ticket_id like %s'''
            cursor.execute(query, (flight_number+"%"))
            last_ticket = cursor.fetchall()
            cursor.close()
            last_ticket = last_ticket['max(ticket_id)']

            for i in range(seats):
                index = i+1+int(last_ticket)
                ticket_id = flight_number + str(index)

                cursor = conn.cursor();
                ins = 'INSERT INTO ticket VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(ins, (ticket_id, airline, flight_number, departure_date, departure_time))
                conn.commit()
                cursor.close()

            return redirect(url_for('/create_flight_confirm'))
    else:
        return redirect(url_for('/login'))

####!!!!!next 30 days???????????????
@app.route('/create_flight_confirm',methods=['GET','POST'])
def create_flight_confirm():
    username = session['username']
    airline = session['airline']
    from_date = date.today()

    cursor = conn.cursor()
    query = '''select * from flight
    where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) >= %s
    and airline_name = %s'''
    cursor.execute(query, (from_date, airline))
    data1 = cursor.fetchall()
    cursor.close()
    return render_template('create-flight-confirm.html',flights=data1)

#--------------add airplane TOTEST------------------
@app.route('/createAirplane',methods=['GET','POST'])
def createAirplane():
    username = session['username']
    usertype = session['usertype']
    if usertype == "staff":
        airline = session['airline']
        airplane_id = request.form['airplane-id']
        seating_capacity = request.form['seating-capacity']

        cursor = conn.cursor();
        query = '''select * from airplane
          where airline_name=%s and id=%s and amount_of_seats=%s'''
        cursor.execute(query, (airline, airplane_id, seating_capacity))
        data = cursor.fetchall()
        cursor.close()

        exist_airplane = None
        if(data):
            return redirect(url_for('/staff_home'),exist_airplane="This airplane already exists.")
        else:
            cursor = conn.cursor();
            ins = 'INSERT INTO airplane VALUES (%s, %s, %s)'
            cursor.execute(ins, (airline, airplane_id, seating_capacity))
            conn.commit()
            cursor.close()
            return redirect(url_for('/create_airplane_confirm'))
    else:
        return redirect(url_for('/login'))

@app.route('/create_airplane_confirm',methods=['GET','POST'])
def create_airplane_confirm():
    username = session['username']
    airline = session['airline']

    cursor = conn.cursor()
    query = '''select id, amount_of_seats from airplane
    where airline_name = %s'''
    cursor.execute(query, (from_date, airline))
    data1 = cursor.fetchall()
    cursor.close()
    return render_template('create-airplane-confirm.html',airplanes=data1,airline=airline)

#--------------add airport TOTEST------------------
@app.route('/createAirport',methods=['GET','POST'])
def createAirport():
    username = session['username']
    usertype = session['usertype']
    if usertype == "staff":
        airport_name = request.form['airport-name']
        city = request.form['city']

        cursor = conn.cursor();
        query = '''select * from airport
          where airport_name=%s and city=%s'''
        cursor.execute(query, (airport_name, city))
        data = cursor.fetchall()
        cursor.close()

        exist_airport = None
        if(data):
            return redirect(url_for('/staff_home'),exist_airport="This airport already exists.")
        else:
            cursor = conn.cursor();
            ins = 'INSERT INTO airport VALUES (%s, %s)'
            cursor.execute(ins, (airport_name, city))
            conn.commit()
            cursor.close()
            return redirect(url_for('/create_airport_confirm'))
    else:
        return redirect(url_for('/login'))

@app.route('/create_airport_confirm',methods=['GET','POST'])
def create_airport_confirm():
    username = session['username']

    cursor = conn.cursor()
    query = '''select * from airport
      where airport_name=%s and city=%s'''
    cursor.execute(query, (airport_name, city))
    data1 = cursor.fetchall()
    cursor.close()
    return render_template('create-airport-confirm.html',airports=data1)

#--------------view flight ratings TODO???--------------


#--------------view frequent customer TODO--------------


#--------------view ticket sales report TODO--------------


#--------------into staff_home: quarterly revenue TODO--------------


#--------------into staff_home: top destinations*2 TODO--------------





#========================END============================
app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
