#!/usr/bin/env python2
#coding: utf8

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(message)s')

import re
import string

def ParseOutYear(text):
    pattern = re.compile(r',\s[1-2][0|8|9][0-9]{2}\s')
    year = pattern.findall(text)

    if year:
        year = remove_punctuation(year[0])
        year = year.strip()
        return year
    else:
        return None

def remove_punctuation(s_in, s_to=u''):
    if isinstance(s_in, unicode):
        not_letters = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
        trans_table = dict((ord(char), s_to) for char in not_letters)
        return s_in.translate(trans_table)
    else:
         return s_in.translate(string.maketrans("", ""), string.punctuation)

def main():
    s1 = r"L Gun-Jae, P Byoung-Uk, Y Dong-Gu… - ICEIC: International …, 2004 - dev02.dbpia.co.kr"
    s2 = "abccc3535"
    s3 = u'CW Wei, YT Kuo, KC Chang, CC Tsai\u2026\xa0- Solid State Circuits\xa0\u2026, 2010 - ieeexplore.ieee.org'
    year = ParseOutYear(s3)
    print year

if __name__ == '__main__':
    main()
