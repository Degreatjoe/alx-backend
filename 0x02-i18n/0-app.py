#!/usr/bin/env python3
"""
this is a simple flask app
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]  # Available languages
    BABEL_DEFAULT_LOCALE = "en"  # Default locale
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app.config.from_object(Config)  # Use Config class for app configuration

# Step 4: Instantiate Babel
babel = Babel(app)


@app.route('/')
def index():
    """
    the index template that it starts with
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
