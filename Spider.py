#!/usr/bin/env python2

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(message)s')

import requests
from bs4 import BeautifulSoup


class Spider:

    def __init__(self, url, page=2, parser='html.parser'):
        self.url = url
        self.page = page
        self.parser = parser
        self.__googleScholarURL = "http://scholar.google.com.tw"

    def crawl(self):
        page_urls = []
        page_urls.append(self.url)
        page_urls += self.__findPages()

        for page_url in page_urls:
            res = requests.get(page_url)
            soup = BeautifulSoup(res.text, self.parser)

            self.__crawlBlock(soup)

    def __findPages(self):
#        logger = logging.getLogger(__findPages.__name__)

        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, self.parser)
        page_url = []

        page_links = soup.select('div[id="gs_nml"] a')
        if not page_links:
#            logger.debug('Can not find the pages link in the start URL')
            pass
        else:
            counter = 0
            for page_link in page_links:
                counter += 1
                if (counter >= self.page):
                    break
                page_url.append(self.__googleScholarURL + page_link['href'])

        return page_url

    def __crawlBlock(self, soup):
        for block in soup.select('div[class="gs_r gs_or gs_scl"]'):
            try:
                print block.select('h3 a')[0].text #Title
            except:
                print "No Title!!!"
                continue

            print "\n"

            try:
                print block.select('h3 a')[0]['href'] #URL
            except:
                print "No URL!!"
                continue

            print "\n"

            try:
                print block.select('div[class="gs_a"]')[0].text #Year
            except:
                print "No Year"

            print "\n"

            try:
                print block.select('div[class="gs_rs"]')[0].text #Content
            except:
                print "No Content!!!!!!!!!!!"
            #Tag
            tag = block.select('div[class="gs_ggsd"] a')
            if tag:
                print tag[0].text
            else:
                print "No Tag!!"
                tag = None
            break
