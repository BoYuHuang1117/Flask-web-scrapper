from flask import Flask
from flask import jsonify

from services.scrapeWeb1 import WebSpiderAMP
from services.scrapeWeb2 import WebSpiderLSVP
from settings import Config

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


    return jsonify(response)