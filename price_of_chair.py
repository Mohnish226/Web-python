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
string_price = element.text.strip() #£129.00

price_without_sign = string_price[1:]
price = float(price_without_sign)

if price <200:
    print("Buy this chair!")
    print("Current price is {}".format(price))
else:
    print("Do not buy this, it's to expensive")