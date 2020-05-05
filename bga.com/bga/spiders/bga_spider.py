# -*- coding: utf-8 -*-
import scrapy
import os
import selectorlib

url_prefix = prefix = 'boardgamearena.com/gamepanel?game='


class BgaSpider(scrapy.Spider):
    name = 'bga_crawler'
    allowed_domains = ['boardgamearena.com']
    """start_urls = ['http://boardgamearena.com/gamelist?section=all']"""
    start_urls = ['https://boardgamearena.com/gamepanel?game=sechsnimmt']

    """# Create extractor for index page
    index_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yml/index.yml'))"""

    # Create extractor for detail page
    detail_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yml/board_game_detail.yml'))



    def parse(self, response):
        # Extract data using Extractor
        data = self.detail_page_extractor.extract(response.text)
        #data = self.detail_page_extractor.extract(response.text)
        yield data

"""div#gamecategory_wrap_all.pagesection div.gamelist_itemrow_inner
div#gamelist_itemrow_inner_all div."""
