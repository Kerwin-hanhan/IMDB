# IMDB Crawler

- 项目名字
  - imdb电影分布式爬虫
  
- 开发环境
  - mongodb + redis + scrapy_redis + scrapy + re 
  
 - 使用技术
  - 通过xpath解析页面
  - 将数据保存在mongodb中
  - url地址去重
    - 使用scrapy_redis 提供的 RFPDupeFilter进行去重
      - 对url进行sha1加密获得指纹
      - 依次将请求方法、url地址、请求体（post数据）update进指纹
      - 放入redis集合中进行去重，实现基于url地址的增量式爬虫

  
