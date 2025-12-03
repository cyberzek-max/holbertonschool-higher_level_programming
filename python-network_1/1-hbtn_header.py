#!/usr/bin/python3
import urllib.request
import sys
"""
This is the module documentation string.
It explains what this script does.
"""
if __name__ == "__main__":
    """
    This script fetches a URL passed as an argument.
    """
    url = sys.argv[1]
    """
    This script fetches a URL passed as an argument.
    """
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        request_id = headers.get('X-Request-Id')
        print(request_id)
