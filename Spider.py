#!/usr/bin/env python2

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(message)s')

import requests
from bs4 import BeautifulSoup
import pdfkit
import time

from ParseOut import ParseOutYear, ParseOutTitle, ParseOutContent, ParseOutTag, ParseOutURL

class Spider:

    def __init__(self, url,
                 p_key=[],
                 n_key=[],
                 score_level=0,
                 key_score={'p': 1, 'n': -3, 'p_none': 1, 'n_none': -1, 'none': -5},
                 weighting={'title': 1.5, 'content': 1},
                 page=5,
                 parser='html.parser',
                 googleScholarURL="http://scholar.google.com.tw"):
        self.url = url
        self.p_key = p_key
        self.n_key = n_key
        self.score_level = score_level
        self.key_score = key_score
        self.weighting = weighting
        self.page = page
        self.parser = parser
        self.__googleScholarURL = googleScholarURL

    def crawl(self):
        logger = logging.getLogger('crawl')
        
        page_urls = []
        page_urls.append(self.url)
        page_urls += self.__findPages()

        results = []
        for index, page_url in enumerate(page_urls):
            res = requests.get(page_url)
            soup = BeautifulSoup(res.text, self.parser)
            print "You are now in page ", (index + 1), " !!!"

            ### Test if the crawler is blocked by the Google robot check
            page_links = soup.select('div[id="gs_nml"] a')
            if not page_links:
                logger.info('1.Google robot check might ban you from crawling!!')
                logger.info('2.You might not crawl the page of google scholar')

            ### Try to crawl the page no matter it might be banned by Google robot check
            results += self.__crawlPage(soup, index + 1)
            time.sleep(4)

        return results

    def __findPages(self):
        logger = logging.getLogger('__findPages')

        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, self.parser)
        page_url = []

        page_links = soup.select('div[id="gs_nml"] a')
        if not page_links:
            logger.debug('Can not find the pages link in the start URL!!')
            logger.info('1.Google robot check might ban you from crawling!!')
            logger.info('2.You might not crawl the page of google scholar')
        else:
            counter = 0
            for page_link in page_links:
                counter += 1
                if (counter >= self.page):
                    break
                page_url.append(self.__googleScholarURL + page_link['href'])

        return page_url

    def __crawlPage(self, soup, page_index):
        logger = logging.getLogger('__crawlBlock')

        counter = 0
        results = []
        blocks = soup.select('div[class="gs_r gs_or gs_scl"]')
        for block in blocks:
            counter += 1
            result = {}
            try:
                b_title = block.select('h3 a')[0].text #Title
                result['b_title'] = b_title
            except:
                ### If there is no title in this block, ignore this block
                logger.debug("No Title in Page %s Block %s", page_index, counter)
                continue

            try:
                b_content = block.select('div[class="gs_rs"]')[0].text #Content
                result['content'] = b_content
            except:
                logger.debug("No Content in Page %s Block %s", page_index, counter)
                result['content'] = None

            try:
                b_url =  block.select('h3 a')[0]['href'] #URL
                b_url = ParseOutURL(b_url)
                result['url'] = b_url
            except:
                ### If there is no URL in this block, ignore this block
                logger.debug("No URL in Page %s Block %s", page_index, counter)
                continue

            try:
                b_year = block.select('div[class="gs_a"]')[0].text #Year
                b_year = ParseOutYear(b_year)
                result['year'] = b_year
            except:
                logger.debug("No Year in Page %s Block %s", page_index, counter)
                result['year'] = None

            ### Check keywords in titles and contents
            ### Evaluate the score of titles and contents by keywords
            f_title, t_score = ParseOutTitle(result['b_title'], self.p_key, self.n_key, self.key_score)
            result['f_title'] = f_title
            content, c_score = ParseOutContent(result['content'], self.p_key, self.n_key, self.key_score)
            result['require'], result['score'] = self.__requireThesis(t_score, c_score)

            ### Record the required thesis with tag.
            ### Set result['tag'], result[tag_link] to None.
            ### If the thesis is required and its tag is [PDF] or [HTML],
            ### set result['tag'] to 'PDF' or 'HTML' and also record the
            ### link in result[tag_link]
            result['tag'] = None
            result['tag_link'] = None
            if result['require']:
                tag = block.select('div[class="gs_ggsd"] a')
                if tag:
                    tag_link = tag[0]['href']
                    tag_text = tag[0].text

                    tag_text = ParseOutTag(tag_text)

                    result['tag'] = tag_text
                    result['tag_link'] = tag_link

            ### Set result['download'] to False,
            ### because the thesis hasn't been downloaded
            result['download'] = False

            ### test only the first link in each page
#            break

            ### Append the information
            ### ('title', 'year', 'content', 'require', 'download')
            ### of the block in results
            results.append(result)

        return results

    def __requireThesis(self, t_score, c_score):
        score = self.weighting['title'] * t_score + self.weighting['content'] * c_score
        if (score > self.score_level):
            return (True, score)
        else:
            return (False, score)

#    def __getPDF(self, url, title, year):
#        res = requests.get(url)
#        print "in __getPDF"
#        f_name = year + " - " + title.strip() + '.pdf'
#        with open(f_name, 'wb') as f:
#            print "Downloading PDF... " + title
#            f.write(res.content)

#    def __getHTML2PDF(self, url, title, year):
#        options = {'page-size': 'A4', 'dpi': 400}
#        f_name = year + " - " + title.strip() + '.pdf'
#        pdfkit.from_url(url, f_name, options = options)
