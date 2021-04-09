#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays\
 the body of the response"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code == requests.codes.ok:
        print(r)
    else:
        print("Error code: {}".format(r.status_code))
