from flask import Flask

from settings import Config

app = Flask("scraper")
app.config.from_object(Config)
