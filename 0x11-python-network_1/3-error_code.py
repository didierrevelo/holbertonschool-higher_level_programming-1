#!/usr/bin/python3
"""Response header value #0
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    reques = Request(url)

    try:
        with urlopen(reques) as request:
            d = request.read()
            print(d.decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
