#!/usr/bin/python3
import urllib.request
import sys
"""Response header value #0
"""
if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
