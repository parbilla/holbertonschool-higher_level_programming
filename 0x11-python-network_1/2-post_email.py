#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL\
 with the email as a parameter, and displays the body of the response"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        mail = response.read()
        print("{}".format(mail.decode()))
