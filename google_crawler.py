#!/usr/bin/env python2

import pickle

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com.tw/scholar?q=frequency+lowering+algorithm&hl=zh-TW&as_sdt=0,5'

    ### p_key and n
    p_key = ['wdrc', 'dynamic range compression', 'hearing aid', 'speech',
             'noise cancellation', 'noise reduction', 'feedback cancellation',
             'sound', 'hearing loss']
    n_key = ['imagery', 'image', 'visual', 'video', 'optic', 'opto', 'quantum',
             'photon']

    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key, page=5)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
