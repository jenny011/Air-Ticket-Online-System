# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from datetime import date

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
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
    from_date = date.today()
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM customer WHERE email = %s and password = %s'
    cursor.execute(query, (username, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    cursor = conn.cursor()
    query = 'select airline_name, flight_number, departure_date, departure_time, ' \
            'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
            'from (flight natural join ticket) join purchase using (ticket_id)' \
            'where email = %s'
         # and departure_date between %s and %s
    cursor.execute(query, (username))
    data1 = cursor.fetchall()
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        return render_template('customer-home.html',from_date=from_date,flights=data1)

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
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-one.html',
                               source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":#####!!!!!!-----todo-------!!!!!!
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination,departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-round.html', source=source, destination=destination,
                               departure_date=departure_date, return_date=return_date, flights=data1)

@app.route("/searchPublicOneWay", methods=['GET', 'POST'])
def searchPublicOneWay():
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination,departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-one.html', source=source, destination=destination, departure_date = departure_date, flights=data1)

    elif triptype == "round":#------!!!!!!!todo
        return_date = request.form['return-date']
        cursor = conn.cursor()
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination,departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, flights=data1)

@app.route("/searchPublicRound", methods=['GET', 'POST'])
def searchPublicRound():
        source = request.form['source']
        destination = request.form['destination']
        triptype = request.form['triptype']
        departure_date = request.form['departure-date']

        if triptype == "one-way":
            cursor = conn.cursor()
            query = 'select * from flight ' \
                    'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                    'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
            cursor.execute(query, (source, destination,departure_date))
            data1 = cursor.fetchall()
            cursor.close()
            return render_template('search-one.html', source=source, destination=destination, departure_date = departure_date, flights=data1)

        elif triptype == "round":#------!!!!!!!todo
            return_date = request.form['return-date']
            cursor = conn.cursor()
            query = 'select * from flight ' \
                    'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                    'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
            cursor.execute(query, (source, destination,departure_date))
            data1 = cursor.fetchall()
            cursor.close()
            return render_template('search-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, flights=data1)


@app.route("/switchPublicView", methods=['GET', 'POST'])
def switchPublicView():
    pass


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
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date)

    elif datetype == "arrival_date":
        cursor = conn.cursor()
        query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight ' \
                'where airline_name = %s and flight_number = %s and arrival_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date)

@app.route("/checkPublic", methods=['GET', 'POST'])
def checkPublic():
    airline_name = request.form['airline-name']
    flight_number = request.form['flight-number']
    datetype = request.form['datetype']
    date = request.form['date']

    if datetype == "departure-date":
        cursor = conn.cursor()
        query = 'select airline_name , flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight ' \
                'where airline_name = %s and flight_number = %s and departure_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        # print(data1)
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date)

    elif datetype == "arrival-date":
        cursor = conn.cursor()
        query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                'from flight ' \
                'where airline_name = %s and flight_number = %s and arrival_date = %s'
        cursor.execute(query, (airline_name, flight_number, date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('check.html', statuses=data1,airline_name=airline_name,flight_number=flight_number,date=date)


# ================ !customer!-home ===================

@app.route('/customer_home')
def customer_home():
    username = session['username']

    cursor = conn.cursor()
    query = 'select airline_name, flight_number, departure_airport, arrival_airport ' \
            'from (flight natural join ticket) join purchase using (ticket_id) ' \
            'where timestamp(cast(arrival_date as datetime)+cast(arrival_time as time)) < now() ' \
            'and email = %s'
    cursor.execute(query, (username))
    data1 = cursor.fetchall()
    print(data1)
    cursor.close()
    return render_template('customer-home.html', unrated=data1)

#---------!customer! search flights-------------
@app.route('/search', methods=['GET', 'POST'])
def search():
    #display the search result
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        # return render_template('search-customer-one.html', source=source, flights=data1)
        return render_template('search-customer-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        pass
        return render_template('search-customer-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, flights=data1)


@app.route('/searchCustomerOneWay', methods=['GET', 'POST'])
def searchCustomerOneWay():
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-customer-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        pass
        return render_template('search-customer-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, flights=data1)

@app.route("/searchCustomerRound", methods=['GET', 'POST'])
def searchCustomerRound():
    source = request.form['source']
    destination = request.form['destination']
    triptype = request.form['triptype']
    departure_date = request.form['departure-date']

    if triptype == "one-way":
        cursor = conn.cursor()
        query = 'select * from flight ' \
                'where timestamp(cast(departure_date as datetime)+cast(departure_time as time)) > now() ' \
                'and departure_airport = %s and arrival_airport = %s and departure_date = %s'
        cursor.execute(query, (source, destination, departure_date))
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('search-customer-one.html', source=source, destination=destination, departure_date=departure_date, flights=data1)

    elif triptype == "round":
        return_date = request.form['return-date']
        pass
        return render_template('search-customer-round.html', source=source, destination=destination, departure_date=departure_date, return_date=return_date, flights=data1)

@app.route("/switchCustomerView", methods=['GET', 'POST'])
def switchCustomerView():
    pass


#------------!customer! view my flights-----------
@app.route('/view', methods=['GET', 'POST'])
def view():
    username = session['username']
    source = request.form['source']
    destination = request.form['destination']
    from_date = request.form['from-date']
    to_date = request.form['to-date']
    if from_date == "/":
        from_date = date.today()
    if to_date == "":
        if source == "/" and destination == "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_date between %s and %s'
            cursor.execute(query, (username, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "/" and destination != "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and arrival_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, destination, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "/" and destination == "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, from_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "/" and destination != "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s and arrival_airport = %s ' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, destination, from_date))
            data1 = cursor.fetchall()
            cursor.close()
    else:
        if source == "/" and destination == "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_date between %s and %s'
            cursor.execute(query, (username, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source == "/" and destination != "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and arrival_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, destination, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "/" and destination == "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
        elif source != "/" and destination == "/":
            cursor = conn.cursor()
            query = 'select airline_name, flight_number, departure_date, departure_time, ' \
                    'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
                    'from (flight natural join ticket) join purchase using (ticket_id)' \
                    'where email = %s and departure_airport = %s and arrival_airport = %s ' \
                    'and departure_date between %s and %s'
            cursor.execute(query, (username, source, destination, from_date, to_date))
            data1 = cursor.fetchall()
            cursor.close()
    return render_template('customer-home.html', from_date=from_date, to_date=to_date,
                           source=source, destination=destination, flights=data1)
    # return render_template('view-customer.html', from_date=from_date, to_date=to_date,
    #                        source=source, destination=destination, flights=data1)

# @app.route("/viewCustomer", methods=['GET', 'POST'])
# def viewCustomer():
#     username = session['username']
#     # viewtype = request.form['viewtype']
#     source = request.form['source']
#     destination = request.form['destination']
#     from_date = request.form['from-date']
#     to_date = request.form['to-date']
#
#     cursor = conn.cursor()
#     query = 'select airline_name, flight_number, departure_date, departure_time, ' \
#             'arrival_date, arrival_time, departure_airport, arrival_airport, status ' \
#             'from (flight natural join ticket) join purchase using (ticket_id)' \
#             'where email = %s and departure_airport = %s and arrival_airport = %s ' \
#             'and departure_date between %s and %s'
#     cursor.execute(query, (username, source, destination, from_date, to_date))
#     data1 = cursor.fetchall()
#     cursor.close()
#     return render_template('view-customer.html', from_date=from_date, to_date=to_date,
#                            source=source, destination=destination, flights=data1)


#Rate TODO

#track TODO


#logout is the same for customer and staff
@app.route('/logout')
def logout():
    session.pop('username')
    return render_template("logout.html")


#=========below I did not edit==========================

@app.route('/home')
def home():
    username = session['username']
    cursor = conn.cursor();
    query = 'SELECT ts, blog_post FROM blog WHERE user_name = %s ORDER BY ts DESC'
    cursor.execute(query, (username))
    data1 = cursor.fetchall()
    for each in data1:
        print(each['blog_post'])
    cursor.close()
    return render_template('home.html', username=username, posts=data1)


@app.route('/post', methods=['GET', 'POST'])
def post():
    username = session['username']
    cursor = conn.cursor();
    blog = request.form['blog']
    query = 'INSERT INTO blog (blog_post, username) VALUES(%s, %s)'
    cursor.execute(query, (blog, username))
    conn.commit()
    cursor.close()
    return redirect(url_for('home'))



app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION


#===============Airline Staff use case============
@app.route('/staff_home')
def staff_home():
    username = session['username']
    cursor = conn.cursor();
    query = 'SELECT * FROM flight WHERE airline_name = %s ORDER BY ts DESC'

    cursor.execute(query, (username))
    data1 = cursor.fetchall()
    for each in data1:
        print(each['blog_post'])
    cursor.close()
    return render_template('home.html', username=username, posts=data1)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
