# -*- coding: utf-8 -*-
# Librarys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Variables
app = Flask(__name__)

# Settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

# Views
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/<libro>/<hoja>', methods=('GET', 'POST'))
def libro(libro, hoja):
	if (hoja =='crear'):
		hoja='se esta creando la hoja'
	return render_template('libro.html', libro=libro, hoja=hoja)

# Run
if __name__ == '__main__':
    app.run()
