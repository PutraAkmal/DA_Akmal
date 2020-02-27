import scrapy
class newSpider(scrapy.Spider):
    name = "new spider"
    start_urls = ['http://172.17.50.43/hr2']
    def parse(self, response):
        css_sel = 'img'
        for x in response.css(css_sel):
            xpath_sel = "@src"
            css_sel = "::attr(src)"
            yield{
                'IMAGE LINK': x.xpath(xpath_sel).extract_first(),
            }
            nextcss_sel = '.next a::attr(href)'
            next_page = response.css(nextcss_sel).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page),callback=self.parse)