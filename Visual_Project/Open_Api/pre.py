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

my_gu = '구로구'

def my_gu_score(my_gu):
    score = pd.read_csv(f'./csv/score.csv', encoding='utf-8')
    total_index = score.점수.count()
    sum_score = sum(score.점수)
    total_avg = sum_score/total_index
    gugu = score[score.구이름.str.contains(my_gu, na=False)]
    gugu = gugu.점수.values
    gu_score = gugu[0]
    print(gu_score)
    print(f'서울 전체평균점수: {total_avg:.2f}점')
    if gu_score > total_avg:
        print('평균보다 크다!')
    elif gu_score < total_avg:
        print('평균보다 작다!')
    else:
        print('equal')
    cnt = 0
    for i in score.구이름:
        # print(i)
        a = score[score.구이름 == i]
        b = a['점수'].values
        # print(b[0])
        if b[0] > gu_score:
            cnt += 1
    print(f'전체구에서 {cnt + 1}등')
    # ,what return
# 평균대비 우리구는 몇% , (구/서울시)/서울
def my_gu_width(my_gu):
    data = pd.read_csv(f'./csv/whole_merged_data2.csv', encoding='utf-8')
    total_index = data.지역명.count()
    # print(total_index)
    # print(data)
    data = data[data.columns.difference(['공원 평균 면적',
                                  '공원 면적 합계','세대',
                                  '인구','구별 총 생산','병원수'])]
    data = data[data.지역명 == my_gu]
    int_data = data.iloc[:,0:-2]
    total_int = int_data.sum(axis=1)
    print(total_int.values)
    print(data.지역명.values)
    print(data['자치구 전체면적'].values)


my_gu_score(my_gu)
my_gu_width(my_gu)



# print('지역명','총합','자치구_전체면적')
# for i in range(1,total_index+1):
#     # print(total_int.iloc[i-1:i].values)
#     b_total = total_int.iloc[i-1:i].values
#     # print(data.지역명.iloc[i-1:i].values)
#     n_total = data.지역명.iloc[i-1:i].values
#     w_total = data['자치구 전체면적'].iloc[i-1:i].values
#     print(n_total[0] ,b_total[0] , w_total[0] )