# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import re
import pandas as pd
import jieba
import jieba.analyse
import operator


url = 'https://www.ptt.cc/bbs/Lifeismoney/M.1623926968.A.2FF.html'
request_headers = {'user-agen':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r = requests.get(url, headers=request_headers)
#確認網頁狀態
#顯示200即為正常
#通常2開頭為正常
#開頭為4或5表示錯誤
print(r.status_code)
# =============================================================================
# #=====================存成html檔案==========================================
# with open('index.html', 'w', encoding="utf-8") as obj:
#     obj.write(r.text)
# #=====================讀取html檔案==========================================
# with open('index.html', 'r', encoding="utf-8") as obj:
#     r = obj.read()
# soup = bs(r, 'lxml')
# =============================================================================
soup = bs(r.text, 'lxml')
category = soup.find('div',{'id':'main-content'}).text
print(category)
