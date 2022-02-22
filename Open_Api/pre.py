# -*- coding:utf-8 -*-
# 파일 공유시 한글파일 명 때문에 에러 발생 --> 임의로 영어로 바꿔줌
import folium
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import json
import seaborn as sns
import matplotlib.pyplot as plt


input_gu = '강남구'
input_file = 'whole_merged_data2.csv'
plt.rcParams['font.family'] = 'Malgun Gothic'

file_data = pd.read_csv(f'./csv/{input_file}',  sep=",")
# gu_width = file_data['자치구 전체면적']
# park_width = file_data['공원 평균 면적']

local = file_data.지역명
cafe = file_data['pet_cafe.json']
together = file_data['together_cafe.json']
diner = file_data['together_diner.json']
# plt.cla()

# ax = sns.barplot(data=file_data,x=local,y=cafe,color='r',alpha = 0.3,label='cafe')
# ax = sns.barplot(data=file_data,x=local,y=together,color = 'b',alpha=0.3,label='together_cafe')
# ax = sns.barplot(data=file_data,x=local,y=diner,color = 'g',alpha=0.3,label='diner')
plt.figure()
ax = plt.bar(x=local,height = cafe,color='r',alpha = 0.3,label='cafe')
ax = plt.bar(x=local,height=together,color = 'b',alpha=0.3,label='together_cafe')
ax = plt.bar(x=local,height=diner,color = 'g',alpha=0.3,label='diner')

plt.legend(loc = 'upper right')
plt.xticks(rotation=45)
plt.ylabel("Count", fontsize = 20)
plt.xlim(-1,25)
plt.show()

# ax = sns.barplot(data=json_json,x=local,y=cafe,color='r',alpha = 0.3,label='cafe')
# ax = sns.barplot(data=json_json,x=local,y=together,color = 'b',alpha=0.3,label='together_cafe')
# ax = sns.barplot(data=json_json,x=local,y=diner,color = 'g',alpha=0.3,label='diner')
#
# plt.legend(loc = 'upper right')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
# ax.set_ylabel("Count", fontsize = 20)
# plt.xlim(-1,25)
# plt.show()