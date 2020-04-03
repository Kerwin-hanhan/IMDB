import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from get_data import data

# 统计IMDB250所属国家前十信息
df = pd.DataFrame(data)

# 对国家进行分类
temp_list = df['countries'].tolist()

# 取出所有国家后去重
country_list = list(set([i for j in temp_list for i in j]))

# 创建一个全为0的DataFrame, columns设为国家
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(country_list))), columns=country_list)

# 将zero_df中出现的国家置为1
for i in range(df.shape[0]):
    zero_df.loc[i, temp_list[i]] = 1

# 按照国家出现频率绘图
sum = zero_df.sum(axis=0)
sum = sum.sort_values(ascending=False).astype(int)[:10]
_x = sum.index
_y = sum.values

plt.figure(figsize=(40, 16), dpi=80)

plt.bar(_x, _y, color='green', alpha=0.4)

plt.savefig("../IMDB_TOP10_COUNTRIES.png")

plt.ylabel("film ouput")
plt.xlabel('country')
plt.title("IMDB250 TOP10 COUNTRIES")

for a, b in zip(_x, _y):
    plt.text(a, b+0.5, b, ha='center', va='bottom')

plt.show()




