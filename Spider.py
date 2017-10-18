#!/usr/bin/env python2

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(message)s')

import requests
from bs4 import BeautifulSoup


class Spider:

    def __init__(self, url, page=5, parser='html.parser'):
        self.url = url
        self.page = page
        self.parser = parser
        self.__googleScholarURL = "http://scholar.google.com.tw"

    def crawl(self):
        page_urls = []
        page_urls.append(self.url)
        page_urls += self.__findPages()

        results = []
        for index, page_url in enumerate(page_urls):
            res = requests.get(page_url)
            soup = BeautifulSoup(res.text, self.parser)

            results.append(self.__crawlBlock(soup, index))

        return results

    def __findPages(self):
        logger = logging.getLogger('__findPages')

        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, self.parser)
        page_url = []

        page_links = soup.select('div[id="gs_nml"] a')
        if not page_links:
            logger.debug('Can not find the pages link in the start URL')
            pass
        else:
            counter = 0
            for page_link in page_links:
                counter += 1
                if (counter >= self.page):
                    break
                page_url.append(self.__googleScholarURL + page_link['href'])

        return page_url

    def __crawlBlock(self, soup, page_index):
        logger = logging.getLogger('__crawlBlock')

        counter = 0
        results = []
        for block in soup.select('div[class="gs_r gs_or gs_scl"]'):
            counter += 1
            result = {}
            try:
                b_title = block.select('h3 a')[0].text #Title
                result['title'] = b_title
            except:
                logger.debug("No Title in Page %s Block %s", page_index, counter)
                continue

            try:
                b_url =  block.select('h3 a')[0]['href'] #URL
                result['url'] = b_url
            except:
                logger.debug("No URL in Page %s Block %s", page_index, counter)
                continue

            try:
                b_year = block.select('div[class="gs_a"]')[0].text #Year
                result['year'] = b_year
            except:
                logger.debug("No URL in Page %s Block %s", page_index, counter)
                result['year'] = None

            try:
                b_content = block.select('div[class="gs_rs"]')[0].text #Content
                result['content'] = b_content
            except:
                logger.debug("No Content in Page %s Block %s", page_index, counter)
                result['content'] = None

            ### check keyword in title and content ###
            results.append(result)
            #Tag
            tag = block.select('div[class="gs_ggsd"] a')
            if tag:
                print tag[0].text
            else:
                print "No Tag!!"
                tag = None
#            break #test only the first link in each page

        return results
