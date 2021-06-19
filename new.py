import requests
from lxml import etree

headers = {"User-Agent":"Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

def search (url):
    res = requests.get(url,headers=headers)
    content = res.content.decode()
    html = etree.HTML(content)
    print(type(html))
    print(html[0])
    #print(str(etree.tostring(html, pretty_print=True),encoding='utf-8'))
    title = []
    title = html.xpath('//tbody//tr/td[3]/h4/a/@title')
    n = 0
    for x in title:
        print(x)
        n += 1
    print(n)        
        


result = search('http://search.books.com.tw/search/query/key/%E4%BC%8A%E5%9D%82%E5%B9%B8%E5%A4%AA%E9%83%8E/cat/all')

print(result)



import requests
from lxml import etree

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

def search (url):
    res = requests.get(url,headers=headers)
    content = res.content.decode()
    html = etree.HTML(content)
    title = html.xpath('//tbody[contains(@id,"")]//tr/td[3]/h4/a/@title')
    link = html.xpath('//tbody[contains(@id,"")]//tr/td[3]/h4/a/@href')
    price = html.xpath('//*[@id="searchlist"]/ul/li/span[@class="price"]/strong[not(contains(text(),"折"))]/b/text()')
    return zip(title,price,link)



//tbody[contains(@id,"")]/tr/td[3]/ul[2]/li/strong[not(contains(text(),"折"))]/text()
//tbody[contains(@id,"")]//tr/td[3]/h4/a/@title