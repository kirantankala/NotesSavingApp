
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():# This function creates and configures the Flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'# Replace with your actual secret key : your_secret_key_here
    
#      secret_key is used by Flask for session management and CSRF protection.
#     #cookies are encrypted using this key.
#      # Make sure to replace 'your_secret_key_here' with a strong, unique secret key for your application.
# # The `create_app` function initializes the Flask application and sets the secret key for session management    
# and CSRF protection.
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'#f''makes the file inside {} as string
#     #we are telling that the database is located in this address
    db.init_app(app)

    from .views import views
    from .auth import auth



# #to access the view and auth these set_url is the url required to redirect to that page 
# #for eg if set_url is '/auth/' then to go to anything in auth we need /auth/{file_name in auth}

    app.register_blueprint(views, url_prefix='/')# Import the views blueprint
    app.register_blueprint(auth, url_prefix='/')# Import the auth blueprint

    from .models import User, Note
        
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app): #if the database exsits it make sure it wont overwrite the new creation
    if not path.exists('website/' + DB_NAME):#if the website dont exist
        db.create_all(app=app)
        print('Created Database!')