# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from scrapers.models import RetsinfoDocument

class RetsinfoItem(DjangoItem):
    django_model = RetsinfoDocument
