# Main code document for SQLAlchemy Homework

# Import Dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

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
        # Proof of work
        f"/api.v1.0/station<br>"
        f"/api.v1.0/measurement<br>"
        # Homework tasks
        f"/api.v1.0/precipitation<br>"
        # Move stations here
        f"/api.v1.0/tobs<br>"
        f"/api.v1.0/tobs2<br>"
        f"/api.v1.0/<start><br>"
        f"/api.v1.0/<start./<end>"

    )

# Set up route to pull station data
@app.route("/api.v1.0/station")
def station():
    # return "This is the station route"

    # Start session to talk to the database
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Station.station, Station.name).all()

    # Close the session
    session.close()

    # Create a dictionary from the data in results
    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)

    # Convert list of tuples into a list to jsonify
    # all_stations = list(np.ravel(results))

    return jsonify(all_stations)

# Set up route to pull measurement data
@app.route("/api.v1.0/measurement")
def measurement():
    # return "This is the measurement route"

    # Start session to talk to database
    session = Session(engine)

    """Return list of measurements"""
    # Query all measurements
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).all()

    # Close the session
    session.close()

    # Create a dictionary from the data in results
    all_measure = []
    for station, date, prcp, tobs in results:
        measure_dict = {}
        measure_dict["station"] = station
        measure_dict["date"] = date
        measure_dict["prcp"] = prcp
        measure_dict["tobs"] = tobs
        all_measure.append(measure_dict)

    return jsonify(all_measure)

# Precipitation route
@app.route("/api.v1.0/precipitation")
def precipitation():
    # Start session
    session = Session(engine)

    """Return list of precipitation and date"""
    # Query measurements for prcp and date
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Close session
    session.close()

    # Set up a dictionary to hold results
    precipitation = []
    for date, prcp in results:
        precip = {}
        precip["date"] = date
        precip["prcp"] = prcp
        precipitation.append(precip)

    return jsonify(precipitation)

# Tobs route
@app.route("/api.v1.0/tobs")
def tobs():
    # Start session
    session = Session(engine)

    """Return list of tobs data"""
    # Query tobs data
    results = session.query(Measurement.date, Measurement.tobs).all()

    # Close session
    session.close()

    return jsonify(tobs_data)

# Tobs data TAKE TWO
@app.route("/api.v1.0/tobs2")
def tobs2():
    # Start the session
    session = Session(engine)

    # Find the most recent date in the data
    most_recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent # 2017-08-03
    query_date = dt.date(2017, 8, 3) - dt.timedelta(days=365)

    # Determine the station with the most observations
    max_station = session.query(func.count(Measurement.tobs), Measurement.station).\
                group_by(Measurement.station).\
                order_by(desc(func.count(Measurement.tobs))).all()
    max_station = max_station[0][1]
    max_station

    """Return list of tobs data"""
    tobs_data = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
            filter(Measurement.date >= query_date).\
            filter(Measurement.station == max_station).all()
    
    # Close session
    session.close()

    return jsonify(tobs_data)

# Stats based on given start date
@app.route("/api.v1.0/<start>")
def start(start):
    # Start session
    session = Session(engine)

    # Caclculate min, max, and average for temps since given start date, inclusive
    temp_stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            order_by(Measurement.date.desc()).all()
    
    # Close session
    session.close()

    return jsonify(temp_stats)
        



# Stats based on given start/end dates
# @app.rout("/api.v1.0/<start./<end>")

















# Base needed code
if __name__ == '__main__':
    app.run(debug=True)