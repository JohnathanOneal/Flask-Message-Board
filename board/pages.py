# !/usr/bin/env/python

from flask import Blueprint

bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return "HOME BOOP"


@bp.route("/about")
def about():
    return "ABOUT BOOP"