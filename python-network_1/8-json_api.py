#!/usr/bin/python3
"""
Sends a r as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    # 1. Handle arguments safely
    # If an argument exists, use it. Otherwise, use an empty string.
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    # 2. Prepare URL and Payload
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}
    # 3. Send POST request
    r = requests.post(url, data=payload)
    # 4. Handle JSON parsing
    try:
        # r.json() attempts to convert the response body to a Python dictionary
        json_data = r.json()

        # Check if the dictionary is empty (e.g., {})
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        # If the body is not valid JSON, r.json() raises a ValueError
        print("Not a valid JSON")
