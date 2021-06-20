# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 23:59:10 2021

@author: OXO
"""
filename0 = "old 20210212.txt"
filename1 = "new 20210616.txt"
   
with open(filename0 , 'r', encoding='utf-8') as f:
    oldlist = f.read().splitlines()
    
with open(filename1 , 'r', encoding='utf-8') as f:
    newlist = f.read().splitlines()
    
#old有 New沒有的
for items in oldlist:
    if items in newlist:
        pass
    else:
        print("已被剔除的股票有")
        print(items)
        
#new有 Old沒有的
for items in newlist:
    if items not in oldlist:
        print(items)
    else:
        pass