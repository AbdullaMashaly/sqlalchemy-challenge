# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        "<br/>"
        f"To return Preciptation analysis: /api/v1.0/precipitation<br/>"
        f"To return available Stations data: /api/v1.0/stations<br/>"
        f"To return Temprature data: /api/v1.0/tobs<br/>"
        f"To return Minimum, Maximum, Average Temprature starting from a certain date: /api/v1.0/YYYY-MM-DD<br/>"
        f"To return Minimum, Maximum, Average Temprature between two dates(first date provided in the API is the start date and the second one is the end date): /api/v1.0/YYYY-MM-DD/YYYY-MM-DD"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    # Convert the query results from your precipitation analysis to a dictionary
    prcp_analysis = []
    for date, prcp in results:
        prcp_dict = {date: prcp}
        prcp_analysis.append(prcp_dict) 

    return jsonify(prcp_analysis)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Measurement.station, Station.name).join(Station, Measurement.station == Station.station).distinct().all()

    stations_list = []
    for station, name in stations:
        stations_dict = {station: name}
        stations_list.append(stations_dict)

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23')\
        .filter(Measurement.station == 'USC00519281').all()

    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {date: tobs}
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def date(start):  

    tobs_info = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs))\
        .filter(Measurement.date >= start).all()

    TMIN = tobs_info[0][0]
    TMAX = tobs_info[0][1]
    TAVG = tobs_info[0][2]
    
    response = (
        f"""The Minimum Temprature is {TMIN},<br/>
        The Maximum Temprature is {TMAX},<br/>
        The Average Temperature is {TAVG}""")
    
    return response

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):   
    
    tobs_info = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs))\
        .filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    TMIN = tobs_info[0][0]
    TMAX = tobs_info[0][1]
    TAVG = tobs_info[0][2]
    
    response = (
        f"""The Minimum Temprature is {TMIN},<br/>
        The Maximum Temprature is {TMAX},<br/>
        The Average Temperature is {TAVG}""")
    
    return response

if __name__ == '__main__':
    app.run(debug=True)