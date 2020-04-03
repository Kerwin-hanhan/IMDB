from pymongo import MongoClient

# 准备数据
client = MongoClient()
collections = client['IMDB']['movie250']
data = collections.find()

