#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:07:57 2020

@author: yafen
"""

from bs4 import BeautifulSoup
import requests
import urllib.request
from PIL import Image
import os
import json

def scraping_sephora(urls):
    lipsticks = []
    for url in urls:
        web = requests.get(url)
        soup = BeautifulSoup(web.content)
        pdlist = soup.find_all('div',class_='css-1ax77m2')
        lipsticks = product_list(pdlist, soup, lipsticks)
    return lipsticks

def product_list(pdlist, soup, lipsticks):
    """input: 
            pdlist - a list of swatch img url scraped from sephora website
            soup - beautiful soup object of a specific product
            lipsticks - an empty list if it's the only product or an existing list with product info in a list of dictionaries
        output: 
            lipsticks - a list of dictionaries with product info including id, brand, looks, color info, urls"""
    for i in range(len(pdlist)):
        brand = soup.find('h1',class_='css-140z8k4').find_all('span')[0].string
        looks = soup.find_all('div',class_='css-1cvjr95')[0].text.split(':')[-1].strip()
        price = soup.find('div',class_='css-slwsq8').span.string
        product_id = pdlist[i].img['src'].split('/')[3].strip('s+w.jpg')
        product_img_url = 'https://www.sephora.com/productimages/sku/s'+product_id+'-main-zoom.jpg?imwidth=60'
        color_img_url = 'https://www.sephora.com'+pdlist[i].img['src']
        color_code = json.loads(soup.find_all('script',{'type': 'application/ld+json'})[1].contents[0])['color'][i]
        c = pdlist[i].button['aria-label'].split(':')
        color = ' '.join(list(set([e for e in c[len(c)-1].strip().split('(')[0].split() if e not in ['-','Selected']])-set(color_code.split())))
#         append all product info as a list of dictionaries to lipsticks
        lipsticks.append({'product_id':product_id,
                            'brand': brand,
                            'looks': looks,  
                            'price': price,
                            'product_img_url': product_img_url,
                             'color_img_url': color_img_url,
                             'color_code': color_code,
                             'color': color})
#         download images of product and the color swatches
        download_img(product_id, product_img_url, color_img_url)
    return lipsticks

def download_img(product_id, product_img_url, color_img_url):
    """download images with specified product_id, image urls"""
#     modify user-agent, which by default assuming a visitor is a python developer
#     by modifying the user-agent, act as if the website is being accessed on a standard web browser by a normal user
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
#     on sephora, the product images are saved as .webp format
    filename_product = '/home/yafen/insight_project/Demos/img_product/'+product_id+'.webp'
    filename_swatch = '/home/yafen/insight_project/Demos/img_swatch/'+product_id+'.jpg'
    urllib.request.urlretrieve(product_img_url,filename_product)
#     after download product image, convert .webp to .jpg format
    im = Image.open(filename_product).convert('RGB')
    im.save('/home/yafen/insight_project/Demos/img_product/'+product_id+'.jpg','jpeg')
#     delete .webp files if exist any
    if os.path.isfile(filename_product):
        os.remove(filename_product)
    urllib.request.urlretrieve(color_img_url,filename_swatch)
