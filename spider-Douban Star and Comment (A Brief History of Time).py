# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:40:48 2018

@author: Luna
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
page = 0
sum = 0
count_star = 0
count_comm = 0

while True:
    html = urlopen("https://book.douban.com/subject/1034282/comments/hot?p="+str(page+1)).read().decode('utf-8')
    pattern =re.compile('<span class="user-stars allstar(.*?)rating"')
    stars =re.findall(pattern,html)
    for star in stars:
        count_star +=1
        if count_star>50:
            break
        else:
            sum += int(star)
            
    soup = BeautifulSoup(html,features='lxml')
    comments = soup.find_all('p','comment-content')
    for comment in comments:
        count_comm +=1
        if count_comm>50:
            break
        else:
            print(count_comm, comment.string)
    page +=1
    if count_comm>50 or count_star>50:
        break
aver = str(sum/count_star/10)
print('\n average star is:'+ aver)




#while True: