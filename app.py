# Main code document for SQLAlchemy Homework

# Import Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up interaction with the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect tables into new model with automap_base
Base = automap_base()
Base.prepare(engine, reflect=True)

# Set up reference to tables
Station = Base.classes.station
Measurement = Base.classes.measurement

# Set up app
app = Flask(__name__)

# Establish necessary framework for webpage
# Define static route
@app.route("/")
def index():
    return (
        f"SQLAlchemy Homework<br>"
        f"/station<br>"
        f"/measurement"
    )

# Set up route to pull station data
@app.route("/station")
def station():
    # return "This is the station route"

    # Start session to talk to the database
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Station.name).all()

    # Close the session
    session.close()

    # Convert list of tuples into a list to jsonify
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

# Set up route to pull measurement data
@app.route("/measurement")
def measurement():
    # return "This is the measurement route"

    # Start session to talk to database
    session = Session(engine)

    """Return list of measurements"""
    # Query all measurements
    results = session.query(Measurement.station).all()

    # Close the session
    session.close()

    # Convert list of tuples into list ot jsonify
    all_measurements = list(np.ravel(results))

    return jsonify(all_measurements)

















# Base needed code
if __name__ == '__main__':
    app.run(debug=True)