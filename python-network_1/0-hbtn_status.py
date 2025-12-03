#!/usr/bin/python3
"""
This is the module documentation string.
It explains what this script does.
"""
import urllib.request

if __name__ == "__main__":
    """
    This script fetches a URL passed as an argument.
    """
    url = "https://intranet.hbtn.io/status"
    bypass_header = {'cfclearance': 'true'}
    with urllib.request.urlopen(url) as response:
        body_bytes = response.read()
        body_string = body_bytes.decode('UTF-8')
        print("- type:" , type(body_bytes))
        print("- content:" , body_bytes)
        print("- utf8 content:" , body_string)
