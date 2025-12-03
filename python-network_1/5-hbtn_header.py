#!/usr/bin/python3
"""
This is the module documentation string.
It explains what this script does.
"""
from requests import *

if __name__ == "__main__":
    """
    This script fetches a URL passed as an argument.
    """
    if __name__ == "__main__":
        url = "https://intranet.hbtn.io/status"
        r = get(url)
        info = r.headers
        print(info.get("X-Request-Id"))
