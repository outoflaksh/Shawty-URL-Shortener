from . import db
from .models import URLs
from flask import Blueprint, render_template, url_for, redirect, request, flash
import string
import random

views = Blueprint("views", __name__)


def shorten_url():
    letters = string.ascii_letters
    digits = string.digits
    seq = random.sample(letters, 3)
    seq.append(random.choice(digits))
    random.shuffle(seq)
    return 's'+''.join(seq)


@views.route("/")
def home():
    #new = request.args["new_url"]
    return render_template("home.html")


@views.route("/", methods=["POST", "GET"])
def url_submit():
    original_url = request.form.get("long-url")
    url_info = URLs.query.filter_by(original_url=original_url).first()

    if url_info:
        flash("URL Already Shortened Once!")
        return redirect(url_for("views.home"))

    short_url = shorten_url()
    while URLs.query.filter_by(created=short_url).first():
        short_url = shorten_url

    new_url = URLs(original_url=original_url, created=short_url)

    db.session.add(new_url)
    db.session.commit()

    return redirect(url_for("views.shortened_url", new=short_url))


@ views.route("/about")
def about():
    return "laksh created this site"


@ views.route("/shortened-url")
def shortened_url():
    try:
        new = request.args["new"]
        return render_template("new_url.html", new_url=request.host_url+new)
    except:
        return render_template("404.html")


@ views.route("/<url_id>")
def redirect_url(url_id):
    url_info = URLs.query.filter_by(created=url_id).first()
    if url_info:
        return redirect(url_info.original_url)
    return render_template("404.html")
