#!/usr/bin/env python3
"""
this module usses getlocale
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    this is the configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


# Step 2: Define get_locale function
@babel.localeselector
def get_locale():
    """
    the get locale function
    """
    # Use request.accept_languages to find the best match
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    the routing function
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
