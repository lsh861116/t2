import scrapy
from mySpider.mySpider.items import DoubanspiderItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start = 0
    url = "https://movie.douban.com/top250?start="
    end = "&filter="
    start_urls = [url+str(start)+end]

    def parse(self, response):
        item = DoubanSpider()
        movies = response.xpath("//div[@class=\'info\']")
        for each in movies:
            title = each.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
            content = each.xpath('div[@class="bd"]/p/text()').extract()
            score = each.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            info = each.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            item['title'] = title
            item['content'] = ";".join(content)
            item['score'] = score[0]
            item['info'] = info[0]

            yield item

        if self.start <=225:
            self.start+=25
            yield scrapy.Request(self.url+str(self.start) + self.end,callback=self.parse)
