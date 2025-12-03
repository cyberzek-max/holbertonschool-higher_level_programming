#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    # 1. Get arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # 2. Prepare the data (Dictionary)
    # requests will automatically URL-encode this for you
    payload = {'email': email}

    # 3. Make the POST request
    # Use data= for form data
    r = requests.post(url, data=payload)

    # 4. Print the body
    # .text automatically decodes the response based on headers
    print(r.text)
