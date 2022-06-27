import os, json
import argparse
import json
import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
import logging
import yaml
import asyncio
from aiohttp import ClientSession

def isHarshad(tempInteger):
    tempString = str(tempInteger)
    sum = 0
    for eC in tempString:
        sum += int(eC)
    if tempInteger % sum == 0:
        return True
    else:
        return False

async def runReport(filter):
    apiConf = {}
    # Load app configurations
    with open("config.yaml", "r") as conf:
        try:
            apiConf = yaml.safe_load(conf)
        except yaml.YAMLError as exc:
            logging.error(exc)

    # Find all cities that match a given filter
    geocoding_url = apiConf['apis']['geocoding_url'] + '?name=' + filter

    # try:
    #     reGeo = requests.get(geocoding_url).text
    # except Timeout:
    #     logging.error("The request timed out.")
    # except requests.exceptions.ConnectionError as re_http:
    #     logging.error("Connection error: " + re_http + ".")

    geocoding_response = ''
    async with ClientSession() as session:
        async with session.get(geocoding_url) as reGeo:
            reGeo = await reGeo.read()
            geocoding_response = json.loads(reGeo)


    # geocoding_response = json.loads(reGeo)

    cityList = []
    harshadList = []
    cityMax = -100000
    cityMin = 100000
    cityMaxName = ''
    cityMinName = ''

    # Check if no results
    if 'results' not in geocoding_response:
        logging.error("No results for search term '" + filter + "'!")
        cityMaxName = 'NA'
        cityMinName = 'NA'
    else:
        # Loop through results to get max min and check for Harshad temperatures
        for el in geocoding_response['results']:
            if el['name'] in cityList:
                continue
            else:
                cityList.append(el['name'])
            long = el['longitude']
            lat = el['latitude']
            forecast_url = apiConf['apis']['forecast_url'] + '?latitude=' + str(lat)
            forecast_url += '&longitude=' + str(long) + '&current_weather=true'

            try:
                reResp = requests.get(forecast_url).text
            except Timeout:
                logging.error("The request timed out.")
            except requests.exceptions.ConnectionError as re_http:
                logging.error("Connection error: " + re_http + ".")

            forecast_response = json.loads(reResp)
            cityTemp = forecast_response['current_weather']['temperature']
            if cityTemp > cityMax:
                cityMaxName = el['name']
                cityMax = cityTemp
            if cityTemp < cityMin:
                cityMinName = el['name']
                cityMin = cityTemp
            if isHarshad(round(cityTemp)):
                harshadDict = dict()
                harshadDict[el['name']] = round(cityTemp)
                harshadList.append(harshadDict)
    
    return cityMaxName, cityMinName, harshadList

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Parse filter parameter from CLI
    descriptionText = 'Returns temperature data related to cities selected using a filter.'
    parser = argparse.ArgumentParser(description=descriptionText)
    helpText = 'String filter to be contained in the city name'
    parser.add_argument('filter', type=str, help=helpText)
    args = parser.parse_args()

    tempHigh, tempLow, tempHarsh = asyncio.run(runReport(args.filter))

    print("Highest Temperature: " + tempHigh)
    print("Lowest Temperature: " + tempLow)
    print("Harshad Temperatures: " + str(tempHarsh))