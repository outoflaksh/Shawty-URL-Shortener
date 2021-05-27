from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def error404(e):
    return render_template("404.html"), 404


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "diafh37r3dw8D8hsh7"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app.register_error_handler(404, error404)

    return app
