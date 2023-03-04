import scrapy

from flask import jsonify
from twisted.internet import reactor

# Current commmand to run "scrapy runspider .\scrapeWeb1.py"
class WebSpiderAMP(scrapy.Spider):
    name = "webspideramp"
    start_urls = ["https://www.amplifypartners.com/portfolio"]
    FILTERED_RESULT = None

    # .status-div
    # .website__link-wr

    def parse(self, response):
        ans = []
        
        for title, website in zip(response.css(".status-div"), response.css(".website__link-wr")):
            status = title.css("::text").get().strip()
            website = website.css("::text").get().strip()
            if status == "Active":
                ans.append(website)

        WebSpiderAMP.FILTERED_RESULT = ans
        yield ans