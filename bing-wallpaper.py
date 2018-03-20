# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 00:35:21 2018

@author: Luna
"""
from urllib.request import urlopen
import urllib
import re

url = 'https://www.bing.com/'
html = urlopen(url).read().decode('utf-8')
pattern = re.compile('/az/.*?.jpg')
images = re.findall(pattern, html)
get=url+images[0]
urllib.request.urlretrieve(get,'download.jpg')