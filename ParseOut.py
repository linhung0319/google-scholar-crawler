#!/usr/bin/env python2
#coding: utf8

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(message)s')

import re
import string

def ParseOutTag(text):
    pattern = re.compile(r'(PDF|HTML)')
    tag = pattern.findall(text)
    if tag:
        return tag[0]
    else:
        tag = None
        return tag

def ParseOutYear(text):
    pattern = re.compile(r',\s[1-2][0|8|9][0-9]{2}\s')
    year = pattern.findall(text)

    if year:
        year = remove_punctuation(year[0])
        year = year.strip()
        return year
    else:
        year = None
        return year

def ParseOutTitle(text, p_key=[], n_key=[], key_score={'p': 1, 'n': -3, 'none': -5}):
    if text:
        title = remove_punctuation(text)
        score = ThesisScore(title, p_key, n_key, key_score)
        return (title, score)
    else:
        title = None
        score = ThesisScore(title, p_key, n_key, key_score)
        return (title, score)

def ParseOutContent(text, p_key=[], n_key=[], key_score={'p': 1, 'n': -3, 'p_none': 1, 'n_none': -1, 'none': -5}):
    if text:
        content = remove_punctuation(text)
        score = ThesisScore(content, p_key, n_key, key_score)
        return (content, score)
    else:
        content = None
        score = ThesisScore(content, p_key, n_key, key_score)
        return (content, score)

def ThesisScore(text, p_key, n_key, key_score):
    score = 0
    ### If there is no text, set score = score + key_score['none']
    if text:
        ### If there is no p_key, set score = score + key_score['p_none']
        if p_key:
            ### If there is one element of p_key in text, set score = score + key_score['p']
            for key in p_key:
                if key.lower() in text.lower():
                    score += key_score['p']
        else:
            score += key_score['p_none']
        ### If there is no n_key, set score = score + key_score['n_none']
        if n_key:
            ### If there is one element of n_key in text, set score = score key_score['n']
            for key in n_key:
                if key.lower() in text.lower():
                    score += key_score['n']
        else:
            score += key_score['n_none']

        return score
    else:
        score += key_score['none']
        return score

def remove_punctuation(s_in, s_to=u' '):
    if isinstance(s_in, unicode):
        not_letters = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~\n'
        trans_table = dict((ord(char), s_to) for char in not_letters)
        return s_in.translate(trans_table)
    else:
         return s_in.translate(string.maketrans("", ""), string.punctuation)

def main():
    s1 = r"L Gun-Jae, P Byoung-Uk, Y Dong-Gu… - ICEIC: International …, 2004 - dev02.dbpia.co.kr"
    s2 = "abccc3535"
    s3 = u'CW Wei, YT Kuo, KC Chang, CC Tsai\u2026\xa0- Solid State Circuits\xa0\u2026, 2010 - ieeexplore.ieee.org'
#    year = ParseOutYear(s3)
#    print year
    p_key = ['wdrc', 'dynamic range compression', 'hearing aids']
    n_key = ['imagery', 'image', 'visual', 'video']
    s4 = u"A fast dynamic range compression with local contrast preservation algorithm and its application to real-time video enhancement"
    s5 = ""
    s6 = u" (WDRC) wdrc"
#    title, score = ParseOutTitle(s6, p_key, n_key)
#    print title
#    print score
    s7 = u'... bank, insertion gain stage, and WDRC for the new Mandarin-specific auditory compensation\nalgorithm, and noise reduction based on entropy and VAD is used to improve speech quality\nand intelligibility. We reduce the power consumption of these algorithms through algorithm ...\n'
#    content, score = ParseOutContent(s7, p_key, n_key)
#    print content
#    print score
    s8 = '[PDF] semanticscholar.org'
    s9 = ''
    tag = ParseOutTag(s8)
    print type(tag)

if __name__ == '__main__':
    main()
