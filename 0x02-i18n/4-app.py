#!/usr/bin/env python3
"""
the module that starts a flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)


class Config:
    """
    the configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Initialize Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    this function gets the locale
    """
    # Check if the 'locale' parameter is in the request args and is valid
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fall back to the best match for supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    this is part of starting the app
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
