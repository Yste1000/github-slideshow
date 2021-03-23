from flask import Blueprint, render_template

# Defining blueprint
views = Blueprint('views', __name__ )

# Establishing the default/home route. Whenever a client enters the default URL (www.aajt.no/ for example), the following function will be run
@views.route('/')
def home():
    return render_template("home.html")