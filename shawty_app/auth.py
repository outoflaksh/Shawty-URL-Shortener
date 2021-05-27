from . import db
from flask import Blueprint, render_template, url_for, redirect

auth = Blueprint("auth", __name__)

@auth.route("/login")
def home():
	return "Login page goes here"

@auth.route("/sign-up")
def about():
	return "sign up goes here"
