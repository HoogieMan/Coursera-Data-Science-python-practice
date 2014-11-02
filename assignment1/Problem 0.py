# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 13:58:24 2014

@author: cjhooger
"""

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
print json.load(response)
