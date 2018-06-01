import scrapy


class woowahan_spider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://www.woowahan.com/#/recruit/tech'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        filename = 'quotes-%s.html'
        print(filename)
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)