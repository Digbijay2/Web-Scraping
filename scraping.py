import scrapy


class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://morvanzhou.github.io/',
    ]
   

    def parse(self, response):
        yield {     # return some results
            'Pages': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'Sub-Pages': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically



# scrapy runspider scraping.py -o res.json
