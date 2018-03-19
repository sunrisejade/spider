# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:26:36 2018

@author: Luna
"""

from urllib.request import urlopen
import re

html= urlopen('http://money.cnn.com/data/dow30/').read().decode('utf-8')
pattern=re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
gets=re.findall(pattern,html)
print(gets)
