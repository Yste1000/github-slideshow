from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__ )

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Running controls before adding the user to the database
        if len(email) < 4:
            # Giving the user a warning if the email is suspiciously short
            flash('Email must be longer than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords are not matching, please check.', category='error')
        elif len(password1) < 7:
            flash('Password needs to be minimum 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
            data = request.form
            print(data)

    return render_template("sign_up.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/home')
def home():
    return render_template("home.html")