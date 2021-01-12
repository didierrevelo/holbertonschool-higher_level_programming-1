#!/usr/bin/python3
import requests
"""
What's my status? #1
"""
html = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(html.text)))
print("\t- content: {}".format(html.text))
