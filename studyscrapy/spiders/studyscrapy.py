from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from studyscrapy.items import StudyscrapyItem


class studyscrapy(CrawlSpider):
    name = 'studyscrapy'
    url = 'https://blog.csdn.net/nav/game'

    start_urls = [
        url,
        # 'http://ip.chinaz.com/getip.aspx',
    ]

    def parse(self, response):
        item = StudyscrapyItem()
        
        selector = Selector(response)
    
        infos = selector.xpath('//*[@id="feedlist_id"]/li')
        print(len(infos))
        print(infos,' ---------------------------------------- ')
        cnt = 0
        for info in infos:
            cnt += 1
            if cnt == len(infos):
                break
            print(info, ' <<<<<< ',cnt)

            title = info.xpath('div/div[2]/h2/a/text()').extract()[0].strip()
            _url = info.xpath('div/div[2]/h2/a/@href').extract()[0]

            item['title'] = title
            item['time'] = _url
            yield item

        urls = [self.url for i in range(2, 20)]
        for url in urls:
        # for _ in range(1000):
            yield Request(self.url, callback=self.parse)
