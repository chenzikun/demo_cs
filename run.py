from flask import Flask
from flask import render_template

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
