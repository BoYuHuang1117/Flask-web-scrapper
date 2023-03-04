from flask import Flask

from SCRAPYMike.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

from SCRAPYMike import scrape_views