#!/usr/bin/env python3
"""
the flask application that uses babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)


class Config:
    """
    the config class for configuring babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    the get locale function get the right locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    the index function starting point of the whole application
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
