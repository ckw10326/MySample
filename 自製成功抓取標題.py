# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:09:19 2021

@author: OXO
"""

import requests
from lxml import etree

headers = {"User-Agent":"Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

def search (url):
    res = requests.get(url,headers=headers)
    content = res.content.decode()
    html = etree.HTML(content)
    print(type(html))
    print(html[0])
    print(str(etree.tostring(html, pretty_print=True),encoding='utf-8'))
    title = []
    link = []
    price = []
    title = html.xpath('//tbody[contains(@id,"")]//tr/td[3]/h4/a/@title')
    link = html.xpath('//tbody[contains(@id,"")]//tr/td[3]/h4/a/@href')
    price = html.xpath('//tbody[contains(@id,"")]/tr/td[3]/ul[2]/li/strong[last()]/text()')
    
    n = 0
    for x in title:
        n += 1
    print("n數量\n\n")
    print(n)    
    m = 0
    for x in link:
        print(x)
        m += 1
    print(m)
    
    
    
result = search('http://search.books.com.tw/search/query/key/%E4%BC%8A%E5%9D%82%E5%B9%B8%E5%A4%AA%E9%83%8E/cat/all')


#//*[@id="itemlist_0010774812"]/tr/td[3]/ul[2]/li/strong[2]