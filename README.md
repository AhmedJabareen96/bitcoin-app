## Welcome to this Simple Python Bitcoin app.

### This a Python web app that gets the current rate of bitcoin in USD, in addition to the average rate in the last 10 minutes.

### The data is also being stored into a Redis database.

## Requirements:

In order to run this project, you will need:

#### Python >= 3.6.

#### PIP for installing python packages.

#### Docker for builing the image

#### Docker Compose for communication between the container image and Redis container.

#### Packages used in this project are:

- Flask for building a simple web REST API.
- Request for reading JSON data from URLs.
- Redis for storing the result of the data being processed.

## Running the application

in order to run the application, use:

> Docker compose up

## Using the application

### To view the current bitcoin price, use:

> curl http://localhost:5000/getNow

### To view the average rate of the last 10 minutes, use:

> curl http://localhost:5000/getAvg

## This project also contains a Jenkins file, in case you want to run it on a Jenkins node.

Please note that, in order to fully work, you have to have your own defined credintials.
[![](pipeline)](https://imgur.com/pb29VOF)

## The resulting image is being pushed into my dockerhub repository.

[![Here is an example of the repository.](docker repo "Here is an example of the repository.")](http://https://imgur.com/a/0CsLJ3Y "Here is an example of the repository.")
