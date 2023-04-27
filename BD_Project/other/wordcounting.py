from konlpy.tag import Okt

from collections import Counter

f= open('filename3.txt','r',encoding='utf-8')
news=f.read()

#Okt 객체 생성
okt = Okt()
noun = okt.nouns(news)
count = Counter(noun)
for i,v in enumerate(noun):
    if len(v)<2:
        noun.pop(i)

count = Counter(noun)
# 명사 빈도 카운트
noun_list = count.most_common(300)
for v in noun_list:
    print(v)

