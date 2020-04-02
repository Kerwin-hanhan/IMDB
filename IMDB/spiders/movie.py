# -*- coding: utf-8 -*-
from logging import getLogger
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
import re

logger = getLogger(__name__)

class MovieSpider(RedisCrawlSpider):
    name = 'movie'
    allowed_domains = ['imdb.com']
    redis_key = 'imdb:start_urls'
    rules = (
        # 匹配位于IMDb Charts的分类页
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='table-row']//a"),), follow=True),
        # 匹配位于Popular Movies by Genre的分类页
        Rule(LinkExtractor(restrict_xpaths=("//li[@class='subnav_item_main']/a"),), follow=True),
        # 匹配翻页
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='lister-page-next next-page']")), follow=True),
        # 匹配Popular Movies by Genre的电影详情页
        Rule(LinkExtractor(restrict_xpaths=("//h3[@class='lister-item-header']/a"),), follow=False, callback='parse_detail'),
        # 匹配电影的详情页
        Rule(LinkExtractor(restrict_xpaths=("//td[@class='titleColumn']/a"), ), follow=False, callback='parse_detail'),
        Rule(LinkExtractor(restrict_xpaths=("//span[@class='trending-list-rank-item-name']/a"), ), follow=False, callback='parse_detail'),
    )

    def parse_detail(self, response):
        # 获取电影详细信息
        data = {}
        # 标题
        data['title'] = response.css('h1::text').extract_first().strip()
        # 分级
        data['rating'] = response.css(
            '.subtext::text').extract_first().strip() or None
        # 时间
        data['year'] = response.css('#titleYear a::text').extract_first()
        # 评分
        data['users_rating'] = response.xpath(
            '//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
        # 票数
        data['votes'] = response.xpath(
            '//span[contains(@itemprop, "ratingCount")]/text()').extract_first()
        # 媒体评分
        data['metascore'] = response.xpath(
            '//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
        # 图片url
        data['img_url'] = response.xpath(
            '//div[contains(@class, "poster")]/a/img/@src').extract_first()
         #国家
        countries = response.xpath(
            '//div[contains(@class, "txt-block") and contains(.//h4, "Country")]/a/text()').extract()
        data['countries'] = [country.strip() for country in countries]
        # 语言
        languages = response.xpath(
            '//div[contains(@class, "txt-block") and contains(.//h4, "Language")]/a/text()').extract()
        data['languages'] = [language.strip() for language in languages]
        # 演员
        actors = response.xpath('//td[not(@class)]/a/text()').extract()
        data['actors'] = [actor.strip() for actor in actors]
        # 分类
        genres = response.xpath(
            "//div[contains(.//h4, 'Genres')]/a/text()").extract()
        data['genre'] = [genre.strip() for genre in genres]
        # 标语
        tagline = response.xpath(
            '//div[contains(string(), "Tagline")]/text()').extract()
        data['tagline'] = ''.join(tagline).strip() or None
        # 描述
        data['description'] = response.xpath(
            '//div[contains(@class, "summary_text")]/text()').extract_first().strip() or None
        # 导演
        directors = response.xpath(
            "//div[contains(@class, 'credit_summary_item') and contains(.//h4, 'Director')]/a/text()").extract() or Non
        if directors:
            data['directors'] = [director.strip() for director in directors]
        # 时间
        data['runtime'] = response.xpath(
            "//div[contains(@class, 'txt-block') and contains(.//h4, 'Runtime')]/time/text()").extract_first() or None
        # url
        data['imdb_url'] = response.url.replace('?ref_=adv_li_tt', '')
        yield data
