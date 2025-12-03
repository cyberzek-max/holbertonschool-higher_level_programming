#!/usr/bin/python3
"""
This is the module documentation string.
It explains what this script does.
"""
from requests import request

if __name__ == "__main__":
    """
    This script fetches a URL passed as an argument.
    """
    if __name__ == "__main__":
        url = "https://intranet.hbtn.io/status"
        r = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
