#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:42:53 2018

@author: Mohnish_Devadiga
"""
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183?colour=Grey")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
#<span itemprop="price" class="now-price"> £129.00 </span>

print(element.text.strip())
#<span itemprop="price" class="now-price"> £129.00 </span>
