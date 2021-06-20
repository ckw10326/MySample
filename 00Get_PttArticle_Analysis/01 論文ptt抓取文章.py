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
soup = bs(r.text, 'lxml')
category = soup.find('div',{'id':'main-content'}).text

# =====================把category存入article.txt檔=============================
# print(category)
# filename = "article.txt"
# with open(filename, 'w', encoding="utf-8" ) as obj:
#     obj.write(category)
# =============================================================================

jieba.set_dictionary('dict_big.txt')
#jieba.load_userdict('1.txt')
words = jieba.cut(category, cut_all = False)
break_words = []
for j in words:
    break_words.append(j)

stopwords = []
for word in open('stopwords.txt', 'r', encoding="utf-8"):
    stopwords.append(word.strip())

del_stopwords = []#用來儲存篩選stopwords詞彙的結果
for k in break_words:
    if k not in stopwords:
        del_stopwords.append(k)
        
#=============================================================================
# 此前del_stopwords為一個List
# 此後把他變成DataFrame
#=============================================================================
df=pd.DataFrame(del_stopwords)
# ==============把Frame寫入df.txt==============================================
# tfile = open('df.txt', 'a',encoding="utf-8")
# tfile.write(df.to_string())
# tfile.close()
# =============================================================================
print(df)
data_clean = df[df[0].str.match('^[\u4e00-\u9fa5]{0,}$')]
print(data_clean)
data_clean.columns=['words']
print(data_clean.columns)
data_clean = data_clean[data_clean.words != '\n']
print(data_clean)
kk = []
for i in range(len(data_clean)):
    kk.append(data_clean.values[i][0])

#=========計算字頻=============================================================
word_count = dict()
for word in kk:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1
    sorted_wc = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)

#=========詞頻統計的結果，分別存成.csv 檔和.txt 檔================
df=pd.DataFrame(sorted_wc)

df.to_csv('ptt數字計算.csv',encoding="utf-8")

# =============================================================================
# f = open('ptt數字計算.txt', 'a', encoding="utf-8")
# for t in range(0,a):
#     f.writelines(xfile[t][0]+ ',' + str(xfile[t][1]) + '\n')
# f.close
# =============================================================================
