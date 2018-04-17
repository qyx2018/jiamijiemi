# -*- coding=utf-8 -*-

import random
import string


#多个字符中选取特定数量的字符：
print ('rand secret num: ')
for i in range(0,10):
     print ("".join(random.sample('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()',32)))

# 随机整数：
print ('rand int: ', random.randint(1,1000))
# 随机选取0到1000间的偶数：
print ('rand even :' ,random.randrange(0, 1000, 2))
# 随机浮点数：
print ('rand float:',random.random())
print ('rand float range:',random.uniform(1, 1000))
# 随机字符：
print ('rand character:',random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'))
# 随机选取字符串：
print ('rand word:',random.choice(['hello', 'world', 'today','fine']))
# 打乱排序
list = [34, 33, 100,3,5,7,8,9,0,6,50];
random.shuffle(list)
print ("rand order : ",  list)
random.shuffle(list)
print ("rand order : ",  list)