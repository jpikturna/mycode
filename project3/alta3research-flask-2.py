#!/user/bin/env python3
"""Project 3: GET  data normalization"""
import requests

# Function to normalize JSON response (break it down to human-readable data)
def normalize_json(json_data):
    normalized_data = {}
    for key, value in json_data.items():
        if isinstance(value, list):
            normalized_data[key] = [item['name'] for item in value]
        else:
            normalized_data[key] = value
    return normalized_data

if __name__ == '__main__':
    url = "http://127.0.0.1:2224/json"  #Flask endpoint
    response = requests.get(url)

    if response.status_code == 200: #(if the request was successful)
        data = response.json()
        normalized_data = normalize_json(data)
        print(normalized_data)
    else:
        print("Failed to retrieve data from the API.") #(if the request was denied or unsuccessful)

