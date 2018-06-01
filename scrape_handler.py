import scrapy

class Spider(scrapy.Spider):
    name = "spidyBoo"

    def start(self, url):
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '/home/jo/Desktop/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file %s " % filename)
