#!/usr/bin/env python2

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com.tw/scholar?start=0&q=wdrc+algorithm&hl=zh-TW&as_sdt=0,5&as_vis=1'

    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url)

    myCrawler.crawl()

if __name__ == '__main__':
    main()
