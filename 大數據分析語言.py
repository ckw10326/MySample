# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 01:16:03 2021

@author: OXO
"""
# =============================================================================
# 
# a = [1,2,3,4,5,6,7,8,9,10,11] 
# b = 12
# c = 0
# for ass in a:
#     if ass < b:
#         pass
#     else:
#         c = 1
# 
# if c==1:
#     print("a列表中有數值大於b")
#     print(c)
# else:
#     print("a列表中數值皆小於b")
#     print(c)
#     
# =============================================================================
    
num = 90
list1 = [1,2,3,56,7,1,5,5,2,6,700]
print("方法2", all(map(lambda x:x <num, list1)))

c = map(lambda x:x <num, list1)
for cs in c:
    print(cs)


print((lambda x:x <num, list1))