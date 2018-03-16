from flask import render_template, redirect, request, session, url_for
from app import app, models, db
from .forms import CustomerForm, OrderForm
# Access the models file to use SQL functions--done
from .models import *

@app.route('/')
def index():
    username = ''
    if "username" in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session["username"]
        # return "Logged in as " + username + '<br>' + \
        # "<b><a href = '/logout'> Click here to log out </a> </b>"
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/login', methods = ["POST", "GET"]) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    if request.method == "POST":
        username = request.form["Name"]
        email = request.form["Email"]
    # session dictionary
        session['username'] = request.form["Name"]
        return redirect(url_for("index"))
    if():
        pass
    return render_template('login.html')

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    form = CustomerForm() 
    if form.validate_on_submit():
        # Get data from the form -- done
        # Send data from form to Database -- done
        trip_name = form.trip_name.data
        destination = form.destination.data
        friend = form.friend.data
        insert_data(trip_name, destination, friend)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    trips =  retrieve_trips([1],[1])
    companions = retrieve_companions([1],[1]) 
    # Retreive data from database to display
    return render_template('home.html',
                            trips=trips, companions=companions)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    customerID = value 
    form2 = OrderForm()
    if form2.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = form2.name_of_part.data
        manufacturer_of_part = form2.manufacturer_of_part.data
        value = value
        insert_orders(name_of_part, manufacturer_of_part, value)
        return redirect('/customers')
    return render_template('order.html', form2=form2, value=value)
