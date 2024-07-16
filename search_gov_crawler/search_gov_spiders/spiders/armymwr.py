from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArmymwrSpider(CrawlSpider):
    name = "armymwr"
    allowed_domains = ["armymwr.com"]
    start_urls = ["https://www.armymwr.com/"]

    rules = (
        Rule(
            LinkExtractor(
                allow=(),
                deny=[
                    "calendar",
                    "location-contact",
                    "DTMO-Site-Map/FileId/",
                    "\*.js",
                    "\*redirect",
                    "\*.xml",
                    "\*.gif",
                    "\*.wmv",
                    "\*.wav",
                    "\*.ibooks",
                    "\*.zip",
                    "\*.css",
                    "\*.mp3",
                    "\*.mp4",
                    "\*.cfm",
                    "\*.jpg",
                    "\*.jpeg",
                    "\*.png",
                    "\*.svg",
                ],
                unique=True,
            ),
            callback="parse_item",
            follow=True,
        ),
    )

    def parse_item(self, response):
        yield {"Link": response.url}
