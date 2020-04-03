from get_data import data
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 绘制排名前15的电影的评分的条形图

df = pd.DataFrame(data)
# 按照评分排序
df = df.sort_values(by='users_rating', ascending=False)[:15][['title', 'users_rating']]
print(df.head())

# 横轴数据设为片名
_x = df['title'].values
print(_x)
# 纵轴数据设为评分
_y = df['users_rating'].values
_y = _y.astype(float)
print(_y)

# 绘制条形图
# 设置显示中文
font = {
    'family': 'Microsoft Yahei',
    'size': 10
}
matplotlib.rc('font', **font)

plt.figure(figsize=(40, 16), dpi=100)

plt.barh(_x, _y, height=0.4, color='purple', alpha=0.4)

plt.xticks([i-0.5 for i in range(1, 11)])

plt.grid(alpha=0.5)

# 添加图例
plt.xlabel("users_rating")
plt.ylabel("title")
plt.title('IMDB TOP 15')

plt.savefig('../IMDB_TOP15.png')

plt.show()


