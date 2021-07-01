# SQLAlchemy_Challenge
Repo for UMN Data Analytics Bootcamp Homework Assignment 10

Tools Used:

* Python
* Pandas
* Matplotlib
* Flask
* SQLAlchemy
* Jupyter Notebook

## Assigment Overview

* Analyze precipitation data from provided dataset using Python and SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use SQLAlchemy to connect to the provided database saved in sqlite.

* Find the most recent date in the dataset and retrieve the last 12 months of precipitation data, returning only the date and precipitation values.

* Load the query results into a Pandas dataframe and sort by date and plot the data.

* Design a query to calculate the total number of stations in the dataset and another query to find the most active station (the station with the highest number of rows of data).

    * Produce a list of stations and identify the one with the highest count of observations.

    * Using the most active station id, design a query to retrieve the last 12 months of temperature data.

    * Plot the results in a histogram with 12 bins

* Create a Flask API app based on the queries established in the Jupyter Notebook with the following routes that return JSONified results:

    * Homepage
    * Precipitation Results
    * Temperature Results
    * Route with a user provided start and end date

* Conduct additional analysis in another Jupyter Notebook

    * Determine if there is a meaningful difference in temperature between June and December and use a t-test to determine if the difference is significant.

    * Calculate the rainfall per weather station using the previous year's matching dates.

    * Calculate the daily normals (averages for the min, avg, and max temperatures) with a function.

    * Load the results of the function into a Pandas dataframe and make an area plot.
