import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

####
# cafe-data.csv

"""
Cafe Name,Location,Open,Close,Coffee,Wifi,Power
Lighthaus,https://goo.gl/maps/2EvhB4oq4gyUXKXx9,11AM, 3:30PM,☕☕☕☕️,💪💪,🔌🔌🔌
Esters,https://goo.gl/maps/13Tjc36HuPWLELaSA,8AM,3PM,☕☕☕☕,💪💪💪,🔌
Ginger & White,https://goo.gl/maps/DqMx2g5LiAqv3pJQ9,7:30AM,5:30PM,☕☕☕,✘,🔌
Mare Street Market,https://goo.gl/maps/ALR8iBiNN6tVfuAA8,8AM,1PM,☕☕,💪💪💪,🔌🔌🔌
Angela's Cafe,https://www.fjlkjlksdjfsdf.com,9AM,5PM,☕☕☕☕☕,💪💪💪,🔌🔌
sdfsdf,https://www.fjlkjlksdjfsdf.com,sdfsdf,sdfsdf,☕️,✘,✘
"""

####
# add.html

"""
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
{{ super() }}
	<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}


{% block title %}Add A New Cafe{% endblock %}


{% block content %}
<div class="container">
  <div class="row">
    <div class="col-sm-12 col-md-8">

      <h1>Add a new cafe into the database</h1>

      {{ wtf.quick_form(form, novalidate=True) }}

	  <p class="space-above"><a href="{{ url_for('cafes') }}">See all cafes</a></p>

    </div>
  </div>
</div>

{% endblock %}
"""

####
# cafes.html


"""
{% extends 'bootstrap/base.html' %}

{% block styles %}
{{ super() }}
	<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}


{% block title %}All Cafes{% endblock %}


{% block content %}

<div class="container">
  <div class="row">
    <div class="col-sm-12">

      <h1>All Cafes</h1>

	  <table class="table">

	  {% for row in cafes %}
	  <tr>
		  	{% for item in row %}
				{% if item[0:4] == "http" %}
				<td><a href="{{ item }}">Maps Link</a></td>
				{% else %}
				<td>{{ item }}</td>
				{% endif %}
			{% endfor %}
	  </tr>
	  {% endfor %}
  	  </table>
      <p><a href="{{ url_for('home') }}">Return to index page</a></p>

    </div>
  </div>
</div>

{% endblock %}
"""

####
# index.html


"""
{% extends 'bootstrap/base.html' %}

{% block styles %}

{{ super() }}
	<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}


{% block title %}Coffee and Wifi{% endblock %}


{% block content %}
<div class="jumbotron text-center">
    <div class="container">
  <h1 class="display-4">☕️ Coffee & Wifi 💻</h1>
  <p class="lead">Want to work in a cafe but need power and wifi?</p>
  <hr class="my-4">
  <p>You've found the right place! Checkout my collection of cafes with data on power socket availability, wifi speed and coffee quality.</p>
  <a class="btn btn-warning btn-lg" href="{{ url_for('cafes') }}" role="button">Show Me!</a>
</div>
    </div>

{% endblock %}
"""
