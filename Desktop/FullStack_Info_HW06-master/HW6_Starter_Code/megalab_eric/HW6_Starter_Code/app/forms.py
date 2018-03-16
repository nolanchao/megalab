from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
    trip_name =  StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = StringField('friend', validators=[DataRequired()])
    # Add additional trip fields here

class OrderForm(Form):
	# Add order input form fields here
	name_of_part = StringField('name_of_part', validators=[DataRequired()])
	manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])