# -*- coding: utf-8 -*-
import scrapy


class MiMobileSpider(scrapy.Spider):
    name = 'mi_mobile'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io/']

    def parse(self, response):
        mobiles = response.xpath("//div[@class='_1UoZlX']")
        for mobile in mobiles:
            yield {
                'name' : mobile.xpath(".//div[@class='_3wU53n']/text()").get(),
                'url' : response.urljoin(mobile.xpath(".//a[@class='_31qSD5']/@href").get()),
                'price' : mobile.xpath(".//div[@class='_1vC4OE _2rQ-NK']/text()").get()

            }

        next_page = response.xpath("//a[@class='_3fVaIS']/@href").get()
        page = response.urljoin(next_page)

        if next_page:
            yield scrapy.Request(url=page, callback=self.parse)
