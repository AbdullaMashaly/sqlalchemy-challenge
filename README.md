# sqlalchemy-challenge
## UNC Data Analytics Bootcamp SQL Alchemy Challenge
In this Scenario, I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decide to do a climate analysis about the area. The following sections outline the steps that I needed to take to accomplish this task.

## Part 1: Analyze and Explore Climate Data

In this section, I performed a climate analysis and data exploration using Python, SQLAlchemy, Pandas, and Matplotlib. I worked with a SQLite database containing climate data.

1. Connect to the database using **create_engine()** and reflect tables using **automap_base()**.

2. Establish a session to interact with the database.

3. Perform a precipitation analysis:
    - Find the most recent date in the dataset.
    - Retrieve the previous 12 months of precipitation data.
    - Load data into a Pandas DataFrame, sort by date, and plot precipitation data using Matplotlib.
    - Print summary statistics for precipitation data.

4. Perform a station analysis:
    - Calculate the total number of stations in the dataset.
    - Find the most-active station (highest observation count) and its temperature statistics.
    - Query the previous 12 months of temperature observation (TOBS) data for the most-active station.
    - Plot a histogram of TOBS data.

## Part 2: Design Flask API

In this part, I created a Flask API based on my analysis and queries:

1. Create a Flask app and define routes:

   - `/`: Display available routes.
   - `/api/v1.0/precipitation`: Get last 12 months of precipitation data as JSON.
   - `/api/v1.0/stations`: Return a JSON list of stations.
   - `/api/v1.0/tobs`: Get temperature observations for most-active station's last year.
   - `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Return JSON lists of temperature statistics for specified date range.

2. Utilize Flask's `jsonify` function to convert data into valid JSON responses.

### Soure code:
- SQLAlchemy 2.0 Documentation <https://docs.sqlalchemy.org/en/20/index.html>
- Flask Documentation <https://flask.palletsprojects.com/en/2.3.x/>
- Python SQLAlchemy – Group_by and return max date <https://www.geeksforgeeks.org/python-sqlalchemy-group_by-and-return-max-date/>
- matplotlib.pyplot <https://matplotlib.org/stable/api/pyplot_summary.html>
- Python Developing Web Applications with Flask <https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python3_Flask.html>
- Default arguments in Python <https://www.geeksforgeeks.org/default-arguments-in-python/>

### References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, <https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml>

