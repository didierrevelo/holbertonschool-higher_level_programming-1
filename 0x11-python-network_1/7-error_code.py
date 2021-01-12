#!/usr/bin/python3
"""Error code #1
"""
import requests
import sys


if __name__ == '__main__':

    data = requests.get(sys.argv[1])
    if data.status_code > 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)
