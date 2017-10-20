#!/usr/bin/env python2

import pickle

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com.tw/scholar?start=0&q=wdrc+algorithm&hl=zh-TW&as_sdt=0,5&as_vis=1'

    ### p_key and n
    p_key = ['wdrc', 'dynamic range compression', 'hearing aid', 'speech']
    n_key = ['imagery', 'image', 'visual', 'video']

    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
