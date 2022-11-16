import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)

#####
# requirements.txt

"""
click==7.1.2
dnspython==2.0.0
dominate==2.5.2
email-validator==1.1.1
Flask==1.0.2
Flask-Bootstrap==3.3.7.1
Flask-WTF==0.14.3
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
visitor==0.1.3
Werkzeug==1.0.1
WTForms==2.3.3"""


####
# login.html

"""
<!DOCTYPE HTML>

<html>
	<head>
		<title>Login</title>
	</head>
	<body>
		<div class="container">
			<h1>Login</h1>
			<form method="POST" action="{{ url_for('login') }}">
			    {{ form.csrf_token }}
			    <p>
				{{ form.email.label }} <br> {{ form.email(size=30) }}
			    </p>
			    <p>
				{{ form.password.label }} <br> {{ form.password(size=30) }}
			    </p>
			    {{ form.submit }}
			</form>
		</div>
	</body>
</html>

"""


####
# base.html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <style>
    {% block styling %}
    body{
        background: purple;
    }
    {% endblock %}
    </style>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
"""



####
# login.html with wtf.quick_form magic

"""
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}
Login
{% endblock %}

{% block content %}
<div class="container">
		<h1>Login</h1>
        {{ wtf.quick_form(form) }}
    </div>
{% endblock %}
"""


####
# denied.html

"""
{% extends 'bootstrap/base.html' %}

{% block title %}
Access Denied
{% endblock %}

{% block content %}
<div class="container">
    <h1>Access Denied </h1>
    <iframe src="https://giphy.com/embed/1xeVd1vr43nHO" width="480" height="271" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cheezburger-funny-dog-fails-1xeVd1vr43nHO">via GIPHY</a></p>
</div>
{% endblock %}
"""


####
# success.html

"""
{% extends 'bootstrap/base.html' %}

{% block title %}
Login
{% endblock %}

{% block content %}
<div class="container">
    <h1>Top Secret </h1>
    <iframe src="https://giphy.com/embed/Ju7l5y9osyymQ" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a></p>
</div>
{% endblock %}
"""


####
# index.html

"""
{% extends 'bootstrap/base.html' %}

{% block title %}
Secrets
{% endblock %}

{% block content %}

<div class="jumbotron">
    <div class="container">
    <h1>Welcome</h1>
    <p>Are you ready to discover my secret?</p>
    <button class="btn btn-primary btn-lg" href=" {{ url_for('login') }} ">Login</button>
    </div>
</div>
{% endblock %}
"""
