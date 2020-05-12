# -*- coding: utf-8 -*-
import scrapy
import os
import selectorlib

opened_file = open(os.path.join(os.path.dirname(__file__), '../selectorlib_yml/gametags.txt') , 'r')
gametags = opened_file.read()
opened_file.close()
big_string = ''.join(gametags)
game_list = big_string.split()
print(game_list)
prefix = 'http://boardgamearena.com/gamepanel?game='
urls = []


for x in game_list:
    #print(x)
    the_url = prefix + x
    urls.append(the_url)


class BgaSpider(scrapy.Spider):
    name = 'bga_crawler'
    allowed_domains = ['boardgamearena.com']
    start_urls = urls



    """start_urls = ['http://boardgamearena.com/gamelist?section=all']"""
    """start_urls = ['https://boardgamearena.com/gamepanel?game=sechsnimmt']"""

    """# Create extractor for index page
    index_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yml/index.yml'))"""

    # Create extractor for detail page
    detail_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yml/board_game_detail.yml'))





    def parse(self, response):
        # Extract data using Extractor
        data = self.detail_page_extractor.extract(response.text)
        #data = self.detail_page_extractor.extract(response.text)
        yield data


