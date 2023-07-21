#!/user/bin/env python3

import requests

# Function to normalize JSON response
def normalize_json(json_data):
    normalized_data = {}
    for key, value in json_data.items():
        if isinstance(value, list):
            normalized_data[key] = [item['name'] for item in value]
        else:
            normalized_data[key] = value
    return normalized_data

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/json"  #Flask endpoint
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        normalized_data = normalize_json(data)
        print(normalized_data)
    else:
        print("Failed to retrieve data from the API.")

