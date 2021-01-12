#!/usr/bin/python3
"""
POST an email #1 
"""
import requests
import sys


url = sys.argv[1]
email = sys.argv[2]
data = requests.post(url, {'email': email})
print(data.text)
