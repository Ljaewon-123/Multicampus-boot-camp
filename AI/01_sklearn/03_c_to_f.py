import numpy as np
import pandas as pd


def celsius_to_fahrenheit(x):
    return (x*1.8)+32

data_C = np.array(range(0,100))
data_F = celsius_to_fahrenheit(data_C)

inp = int(input('섭씨 온도를 입력해 주세요 '))
print(inp,'는 화씨',celsius_to_fahrenheit(inp),'입니다')