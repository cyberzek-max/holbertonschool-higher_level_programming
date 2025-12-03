#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    # requests.get supports Basic Auth directly via the 'auth' parameter
    r = requests.get(url, auth=(username, password))
    # We use .get('id') so it returns None if the key doesn't exist
    # (e.g. on authentication failure)
    print(r.json().get('id'))
