#!/usr/bin/env python3
"""Work with ISS data via API access"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    
    long = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    
    time = resp["timestamp"]
    time = datetime.datetime.fromtimestamp(time)
        
    locator_resp = rg.search((lat, long))

    city = locator_resp[0]["name"]

    country = locator_resp[0]["cc"]

    print(f"Current Location: {long} LONG, {lat} LAT")
    print(f"Timestamp:  {time}")
    print(f"City/Country: {city}, {country}")

if __name__ == "__main__":
    main()

