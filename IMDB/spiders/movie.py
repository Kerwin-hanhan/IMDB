# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
import re


class MovieSpider(RedisCrawlSpider):
    name = 'movie'
    allowed_domains = ['imdb.com']
    redis_key = 'imdb'
    rules = (
        # 匹配位于IMDb Charts的分类页
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='table-row']"),), follow=True),
        # 匹配位于Popular Movies by Genre的分类页
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='quicklinks']"),), follow=True),
        # 匹配IMDb Charts的电影的详情页
        Rule(LinkExtractor(restrict_xpaths=("//td[@class='titleColumn']/a"),), follow=False, callback='parse_detail'),
        # 匹配翻页
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='lister-page-next next-page']")), follow=True),
        # 匹配Popular Movies by Genre的电影详情页
        Rule(LinkExtractor(restrict_xpaths=("//h3[@class='lister-item-header']"),), follow=False, callback='parse_detail')
    )

    def parse_detail(self, response):
        # 获取电影详细信息
        item = {}
        print("start_parse")
        # 标题
        item['title'] = response.xpath("//div[@class='title_wrapper']/h1/text()").extract_first()
        # 上映年份
        item['year'] = response.xpath("//div[@class='subtext']/a[last()]/text()").extract_first()
        # 电影时长
        item['length'] = response.xpath("//div[@class='txt-block']/time/text()").extract_first()
        # 评分
        item['rating'] = response.xpath("//span[@itemprop='ratingValue']/text()").extract_first()
        # 票房
        item['box'] = response.xpath("//div[@id='titleDetails']//h4[text()='Cumulative Worldwide Gross:']/../text()").extract()
        # 匹配分类
        item['cate'] = re.findall(r"\"genre\": \[(.*?)\]", response.body.decode(), re.S)
        yield item
