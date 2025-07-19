
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   #means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#this contain login logout signin routes

@auth.route('/login',methods=['GET','POST']) #this is the endpoint for the login and this is how its created
def login():#this is the function for the endpoint created
    if request.method == 'POST':#if we are signing in 
         email = request.form.get('email')
         password = request.form.get('password')

         user = User.query.filter_by(email=email).first()#if we are looking for a specific user having this email and also return the first user
         if user:
             if check_password_hash(user.password, password):
                 flash('Logged in successfully!', category='success')
                 login_user(user, remember=True)
                 return redirect(url_for('views.home'))
             else:
                 flash('Incorrect password, try again.', category='error')
         else:
             flash('Email does not exist.', category='error')
    return render_template("login.html",user=current_user)#this directs towards template used in the html code




@auth.route('/logout')
@login_required#this ensures that we cant logout unless we login into the pages
def logout():
     logout_user()
     return redirect(url_for('auth.login'))



@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
      email = request.form.get('email')
      first_name = request.form.get('firstName')
      password1 = request.form.get('password1')
      password2 = request.form.get('password2')
    
      user=User.query.filter_by(email=email).first()
      if user:
           flash("Email already exists",category='error')
     
      elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')#category can be error or sucess
      elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
      elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
      elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
      else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            #hash generates a hash for password verification
            #'pbkdf2:sha256' is the correct and secure method supported for password hashing.
            db.session.add(new_user)#adding the new user to the database
            db.session.commit()#commiting that the user is added into the database
            login_user(new_user, remember=True)  
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))#redirecting the url to the home page in the views 

    return render_template("sign_up.html",user=current_user)




# from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from . import db   ##means from __init__.py import db
# from flask_login import login_user, login_required, logout_user, current_user


# auth = Blueprint('auth', __name__)


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 flash('Logged in successfully!', category='success')
#                 login_user(user, remember=True)
#                 return redirect(url_for('views.home'))
#             else:
#                 flash('Incorrect password, try again.', category='error')
#         else:
#             flash('Email does not exist.', category='error')

#     return render_template("login.html", user=current_user)


# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))


# @auth.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already exists.', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(first_name) < 2:
#             flash('First name must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(email=email, first_name=first_name, password=generate_password_hash(
#                 password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account created!', category='success')
#             return redirect(url_for('views.home'))

#     return render_template("sign_up.html", user=current_user)