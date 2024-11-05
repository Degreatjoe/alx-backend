#!/usr/bin/env python3
"""
this modules starts a flask app but also adds the babel
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


# Step 3: Define Config Class
class Config:
    """
    this class configures the babel
    """
    LANGUAGES = ["en", "fr"]  # Available languages
    BABEL_DEFAULT_LOCALE = "en"  # Default locale
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app.config.from_object(Config)  # Use Config class for app configuration

# Step 4: Instantiate Babel
babel = Babel(app)


@app.route('/')
def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
