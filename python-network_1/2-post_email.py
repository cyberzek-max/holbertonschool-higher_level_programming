#!/usr/bin/python3
"""
This is the module documentation string.
It explains what this script does.
"""
import urllib.request
import sys
if __name__ == "__main__":
    """
    This script fetches a URL passed as an argument.
    """
    url = sys.argv[1]
    email = sys.argv[2]
    """
    This script fetches a URL passed as an argument.
    """
    data = {"email": email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data, method='POST')
    with urllib.request.urlopen(req) as response:
        response_body = response.read()
        body_string = response_body.decode('UTF-8')
        print(body_string)
