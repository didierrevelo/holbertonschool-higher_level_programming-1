#!/usr/bin/python3
"""
 POST an email #0
"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    value = {'email': mail}
    dat = urllib.parse.urlencode(value)
    dat = dat.encode('ascii')
    request = urllib.request.Request(url, dat)
    with urllib.request.urlopen(request) as response:
        html = response.read().decode('utf-8')
        print(html)
