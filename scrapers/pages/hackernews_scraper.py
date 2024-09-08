from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Rule
from scrapers.scraper import ScrapedItem, Scraper
import scrapy


class ArticleItem(ScrapedItem):
    """
    Article class for scraped items
    """
    title = scrapy.Field()
    url = scrapy.Field()


class HackernewsSpider(Scraper):
    """
    HackernewsSpider class for all scraping operation
    """
    name = 'pythonhackernews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/news?p=1']

    rules = (Rule(LinkExtractor(allow=r'news\?p=[0-2]'),
                callback="parse-item",
                follow=True),)

    def parse_item(self, response):
        """
        Method that parses scraped items
        """
        items = []
        selector = Selector(response)
        links = selector.xpath('//td[@class="title"]').xpath('//span[@class="titleline"]')

        for link in links:
            title = link.xpath("a/text()").extract()
            url = link.xpath("a/@href").extract()

            if title and url:
                title, url = title[0], url[0]
                # print(f'{title} and {url} \n')

                item = ArticleItem()
                item['title'] = title
                item['url'] = url

                items.append(item)
                yield item # items

    def closed(self, reason):
        print(f"Spider finished scraping. Reason: {reason}")
