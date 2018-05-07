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

    def start_requests(self):
        # urls = [self.url for i in range(1, 20)]
        # for url in urls:
        while True:
            for _ in range(10):
                yield Request(self.url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        self.log(' >>>>>>>>>>>>>>>>>> 点开<首页>的URL了 <<<<<<<<<<<<<<<<<< ')

        selector = Selector(response)
        infos = selector.xpath('//*[@id="feedlist_id"]/li')

        # print(len(infos))
        # print(infos,' ---------------------------------------- ')
        
        cnt = 0
        for info in infos:
            cnt += 1
            if cnt == len(infos):
                break

            # print(info, ' <<<<<< ',cnt)

            # title = info.xpath('div/div[2]/h2/a/text()').extract()[0].strip()
            _url = info.xpath('div/div[2]/h2/a/@href').extract()[0]

            yield Request(url=_url, callback=self.parse)

    def parse(self, response):
        # 将我们需要的数据都解析出来 并交给CsdnspiderPipeline管道处理
        self.log(' >>>>>>>>>>>>>>>>>> 点开文章的URL了 <<<<<<<<<<<<<<<<<< ')
        item = StudyscrapyItem()
        selector = Selector(response)
        # article_title = selector.css('.title-articlel')
        # created_time = selector.css('.time')

        article_title = selector.xpath('//h6[@class="title-article"]/text()').extract()[0]
        created_time = selector.xpath('//span[@class="time"]/text()').extract()[0]

        # print(type(article_title))
        # print(article_title)
        # print(type(created_time))
        # print(created_time)

        item['title'] = article_title
        item['time'] = created_time

        yield item


