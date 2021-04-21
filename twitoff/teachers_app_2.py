"""This is what brings the application together"""
from flask import Flask, render_template
from .models import DB, User
from .twitter import add_or_update_user


def create_app():
    """
    The main app function for twitoff.
    Brings everything together.
    """
    # __name__ is the name of the current path module
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        # Drops everything from DB
        DB.drop_all()
        # Creates DB
        DB.create_all()
        return render_template('base.html', title="Home")

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return "Database reset!"

    @app.route('/addusers')
    def add_users():
        # adding users
        add_or_update_user("elonmusk")

    return app
