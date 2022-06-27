# Python Coding Challenge

## Problem Description

This exercise consists on writing a Python application that uses a couple of APIs  to fetch, parse and expose data:
* [**Geocoding API**](https://open-meteo.com/en/docs/geocoding-api)
* [**Weather Forecast API**](https://open-meteo.com/en/docs)

These are the requirements:

* Use `config.yaml` as the source of configuration(s) for your application;
* Use the Geocoding API to request and find all the cities that match a given query;
* Use the Weather Forecast API to get the current temperature for each city (Free tip: lookup for current_weather)
* Among the results, find the city with the highest and the lowest temperature;
* Find the cities in which the temperature is a Harshad Number:
    A [**Harshad number**](https://en.wikipedia.org/wiki/Harshad_number) is a number which is divisible by the sum of its digits. For example, `132` is divisible by `6` (1+3+2). By default a temperature value will be a float, you might need to treat it as an unsigned integer;
* Create a docker image that ships the `coding_challenge.py` content and runs it in a containerized environment. 
    It should print a list of the Harshad temperatures to the command line;
* The application should be Production ready.

##  Expected usage using the filter 'San' (results might differ):

``` bash
 > docker run challenge San
Highest Temperature: Santos
Lowest Temperature: San Juan
Harshad Temperatures: [{'San Diego': 20}, {'San Jose': 24}, {'Sanaa': 18}, {'San Juan': 12}, {'Santa Fe': 20}]
```