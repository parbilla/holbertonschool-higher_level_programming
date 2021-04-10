#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user"""
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    dict = {'q': letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=dict)
    try:
        result = r.json()
        if 'id' in result and 'name' in result:
            print("[{}] {}" .format(result['id'], result['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
