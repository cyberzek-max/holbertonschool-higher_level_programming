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
    bypass_header = {'cfclearance': 'true'}
    try:
        with urllib.request.urlopen(url) as response:
            body_bytes = response.read()
            body_string = body_bytes.decode('UTF-8')
            print(body_string)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
