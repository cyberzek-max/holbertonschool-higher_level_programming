#!/usr/bin/python3
"""
This is the module documentation string.
It explains what this script does.
"""
from requests import *
from sys import *

if __name__ == "__main__":
    """
    This script fetches a URL passed as an argument.
    """
    url = argv[1]
    email = argv[2]
    """
    This script fetches a URL passed as an argument.
    """
    data = {"email": email}
    encoded_data = urlencode(data).encode('utf-8')
    req = Request(url, data=encoded_data, method='POST')
    with urlopen(req) as response:
        response_body = response.read()
        body_string = response_body.decode('UTF-8')
        print(body_string)
