from flask import Flask
from flask import jsonify

from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy import signals
from services.scrapeWeb1 import WebSpiderAMP
from services.scrapeWeb2 import WebSpiderLSVP
from settings import Config

from twisted.internet import reactor

app = Flask(__name__)
app.config.from_object(Config)

""" API definition """

@app.route("/", methods=["GET"])
def home():
    return jsonify(msg="Welcome to Michael's scraper!!")


@app.route("/api/scrape-all", methods=["GET"])
def scrape():
    # "https://www.amplifypartners.com/portfolio"
    # "https://lsvp.com/portfolio/"
    response = {}
    
    runner = CrawlerRunner()
    runner.crawl(WebSpiderAMP)
    runner.crawl(WebSpiderLSVP)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(0)

    # print(WebSpiderAMP.FILTERED_RESULT)
    # print(WebSpiderLSVP.FILTERED_RESULT)

    response["amplifypartners.com"] = WebSpiderAMP.FILTERED_RESULT
    response["lsvp.com"] = WebSpiderLSVP.FILTERED_RESULT
    return jsonify(response)
