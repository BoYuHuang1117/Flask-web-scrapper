import scrapy

class WebSpiderLSVP(scrapy.Spider):
    name = "webspiderlsvp"
    start_urls = ["https://lsvp.com/portfolio/"]
    FILTERED_RESULT = None
    # .txt
    # .url

    def parse(self, response):
        ans = []
        for text, url, status in zip(response.css(".txt")[:-1], response.css(".url"), response.css(".subtitle")):
            name = text.xpath("h2").css("::text").get().strip()
            url = url.css("::text").get().strip()
            status = status.css("::text").get().strip().lower()

            if "acquired" not in status and "public" not in status:
                ans.append(url)
        
        WebSpiderLSVP.FILTERED_RESULT = ans
        yield ans