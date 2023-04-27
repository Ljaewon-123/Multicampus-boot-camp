import pandas as pd
import json
from pandas import json_normalize
import csv


# json형태의 데이터(사고다발지역 지점)를 변수에 넣어준다.

json_file_path="./namename3.json"

with open(json_file_path,'r', encoding='utf-8') as j:
    contents=json.loads(j.read())


# json형태(년도가 key)의 데이터를 넣어주면 csv파일로 바꿔준다.
def json_to_csv(x):
    data = []
    df = pd.DataFrame()
    for n in x.keys():
        json = x[n]
        for i in range(len(json)):
            for j in json[i]:
                for k in range(len(json[i][j])):
                    for l in json[i][j][k]:
                        for m in range(len(json[i][j][k][l])):
                            data.append(list(json[i][j][k][l][m].values()))
                            columns = json[i][j][k][l][m].keys()
        year_df = pd.DataFrame(data,columns=columns)
        year_df['발생년도'] = n
        df = pd.concat([df, year_df], ignore_index=True)
    
    # 입력받은 파라미터가 파일 이름에 쓰인다.
    # 예) json형태의 변수 child를 넣어주면 'child_accident.csv'로 저장된다.
    vnames = [name for name in globals() if globals()[name] is x]
    df.to_csv(f'{vnames[0]}_accident.csv')
    return df

json_to_csv(contents)