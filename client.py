#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 02:32:08 2020

@author: 96abdou96
"""

from __future__ import print_function
import requests
import json

addr = 'http://localhost:5000'
test_url = addr + '/'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}


files = [
    ('image', ('lenna', open('./lenna.png', 'rb'), 'image/png')),
    ('data', ('data', json.dumps({'length' : '70'}), 'application/json')),
]

response = requests.post(test_url, files = files)

to_display = json.loads(response.text)

file1 = open("art.txt","w+")

file1.write(to_display['art'])

file1.close()
# decode response
#print(json.loads(response.text))