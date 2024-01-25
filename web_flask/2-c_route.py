#!/usr/bin/python3
"""
Script that starts a Flask web application.

This script defines a simple Flask web application with three routes:
1. '/' - Displays 'Hello HBNB!'
2. '/hbnb' - Displays 'HBNB'
3. '/c/<text>' - Displays 'C ' followed by the value of the text variable
   (replace underscore '_' symbols with a space ' ').

Usage:
Run this script, and the web application will be accessible on http://0.0.0.0:5000/.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'

    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB'

    Returns:
        str: "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'C ' followed by the value of the text variable
    (replace underscore '_' symbols with a space ' ').

    Args:
        text (str): The value provided in the URL.

    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

