import codecs 
import jieba
from collections import Counter  
  
def get_words(txt):  
    seg_list = jieba.cut(txt)  
    c = Counter()  
    for x in seg_list:  
        if len(x)>1 and x != '\r\n':  
            c[x] += 1  
    print('词频统计')  
    for (k,v) in c.most_common(100):  
        print('%s%s %s  %d' % ('  '*(5-len(k)), k, '*'*int(v/3), v))  
   
if __name__ == '__main__':  
    with codecs.open('YuGiOh.txt', 'r', 'utf8') as f:  
        txt = f.read()  
    get_words(txt)  