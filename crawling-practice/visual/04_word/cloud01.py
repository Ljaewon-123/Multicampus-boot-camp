from wordcloud import WordCloud
import json

cloud = WordCloud(font_path='Goyang.ttf',background_color='white',max_words=30,width=400,height=300)

with open('webtoons.json',encoding='utf-8') as f:
    webtoons = json.load(f)

# print(webtoons)
res = dict()
for webtoon in webtoons['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) * 100)

visual = cloud.fit_words(res)
visual.to_image()
visual.to_file('cloud01.png')