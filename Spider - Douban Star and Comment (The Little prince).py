from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = 0
sum_star=0
count_star=0
count_comm=0

while True:

    html=urlopen('https://book.douban.com/subject/1084336/comments/hot?p='+str(page+1)).read().decode('utf-8')

    pattern=re.compile('<span class="user-stars allstar(.*?)rating"')
    tags=re.findall(pattern,html)
    for tag in tags:
        count_star=count_star+1
        if count_star>50:
            break
        else:
            sum_star += int(tag)

    soup=BeautifulSoup(html,features='lxml')
    comments=soup.find_all('p','comment-content')
    for comment in comments:
        count_comm=count_comm+1
        if count_comm>50:
            break
        else:
            print(count_comm,comment.string)

    page=page+1

    if count_comm>50 or count_star>50:
        break

ave_star=str(sum_star/count_star/10)
print('Average Star is: '+ave_star)
