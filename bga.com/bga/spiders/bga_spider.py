# -*- coding: utf-8 -*-
import scrapy
import os
import selectorlib


class BgaSpider(scrapy.Spider):
    name = 'bga_crawler'
    allowed_domains = ['boardgamearena.com']
    """start_urls = ['http://boardgamearena.com/gamelist?section=all']"""
    start_urls = ['https://boardgamearena.com/gamepanel?game=raceforthegalaxy']
    # Create extractor for detail page
    detail_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yml/board_game_detail.yml'))



    def parse(self, response):
        # Extract data using Extractor
        data = self.detail_page_extractor.extract(response.text)
        yield data
