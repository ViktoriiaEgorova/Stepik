#r=float(input())
#import math
#print(2*math.pi*r)


#import sys
#lst=sys.argv
#del lst[0]
#for i in range(0,len(lst)):
#    print(lst[i], end=' ')

import requests
lines = 0
with open ('E:\Download\dataset_3378_2.txt', 'r') as site: # считываем ссылку из скаченного файла
 site = site.read().strip()
 filo = requests.get(site) # GET запрос по полученой ранее ссылке
 for i in filo.text.splitlines(): # считаем строки в файле
    lines += 1
print(lines)