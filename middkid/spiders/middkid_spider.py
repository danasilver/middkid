import scrapy

from middkid.items import MiddKidItem

class MiddKidSpider(scrapy.Spider):
    name = 'middkid'
    allowed_domains = ['middkid.com']
    start_urls = [
        'http://middkid.com/course-evaluations/'
    ]

    def parse(self, response):
        for url in response.css('ul.list-terms a::attr("href")').extract():
            yield scrapy.Request(url, callback=self.parse_department)

    def parse_department(self, response):
        for url in response.css('ul.list-professors a[title="View Ratings"]::attr("href")').extract():
            yield scrapy.Request(url, callback=self.parse_prof_course)

    def parse_prof_course(self, response):
        prof_course = MiddKidItem()
        prof_course['review_count'] = len(response.css('.comment').extract())
        prof_course['code'] = response.css('.entry-title small::text').extract()[0][1:-1]
        prof_course['name'] = response.css('.entry-title::text').extract()[0]
        prof_course['professor'] = response.css('.evaluate-professor::text').extract()[0].strip()
        prof_course['url'] = response.url
        yield prof_course
