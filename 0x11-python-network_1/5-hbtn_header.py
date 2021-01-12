#!/usr/bin/python3
"""Response header value #0
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    data = requests.get(url)
    print(data.headers.get('X-Request-Id'))
