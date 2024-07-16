"""Module for running on EC2 instance."""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from search_gov_crawler.search_gov_spiders.spiders.armymwr import ArmymwrSpider
from search_gov_crawler.search_gov_spiders.spiders.domain_spider import DomainSpider


def hello_world():
    """_summary_"""
    print("Hello World")


def run_test_spider():
    """_summary_"""
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        }
    )
    process.crawl(ArmymwrSpider)
    process.start()  # the script will block here until the crawling is finished


def run_all_domains():
    """_summary_"""
    process = CrawlerProcess(get_project_settings())
    process.crawl(DomainSpider)
    process.start()
