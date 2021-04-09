#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays\
 the body of the response"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
