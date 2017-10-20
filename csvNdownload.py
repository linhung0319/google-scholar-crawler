#!/usr/bin/env python2

import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pdfkit

def ThesisNeedDownload(df):
    ### Write the required thesis [title, year, url] which
    ### need to be downloaded to a DataFrame and output the
    ### DataFrame to a csv file
    df_table = df[df.tag.isnull() == True][df.require == True][['b_title', 'year', 'url']]
    df_table = df_table.sort_values(by=['year'], ascending=[False])
    title = 'ThesisNeedDownload.csv'
    df_table.to_csv(("./CSV/" + title), encoding='utf-8')

def ThesisPDFDownload(df):
    ### Download the PDF file which has the PDF tag
    df_table = df[df.tag == 'PDF'][['f_title', 'year', 'tag_link']]
    for index, row in df_table.iterrows():
        title = str(row['year']) + ' - ' + row['f_title'] + '.pdf'
        url = row['tag_link']
        print title
        print url
        try:
            res = requests.get(url)
            if (res.status_code == 200):
                with open(("./PDF/" + title), 'wb') as f:
                    print "Downloading PDF... "
                    f.write(res.content)
                    df.at[index, 'download'] = True
        except:
            print "Can not download the PDF file"

def ThesisHTMLDownload(df):
    ### Download the HTML file which has the HTML tag and output a PDF file
    options = {'page-size': 'A4', 'dpi': 400}
    df_table = df[df.tag == 'HTML'][['f_title', 'year', 'tag_link']]
    for index, row in df_table.iterrows():
        title = str(row['year']) + ' - ' + row['f_title'] + '.pdf'
        url = row['tag_link']
        print title
        print url
        try:
            pdfkit.from_url(url, ("./HTML/" + title), options=options)
            df.at[index, 'download'] = True
        except:
            print "Can not download the HTML file"

def Thesis(df):
    ### Write all the required thesis [title, year, download] in csv file
    df_table = df[df.require == True][['b_title', 'year', 'download']]
    df_table = df_table.sort_values(by=['year'], ascending=[False])
    title = 'ThesisTitle.csv'
    df_table.to_csv(("./CSV/" + title), encoding='utf-8')

def main():

    with open('result.pickle', 'rb') as f:
        result = pickle.load(f)

    df = pd.DataFrame(result)

    ThesisNeedDownload(df)

    ThesisPDFDownload(df)

    ThesisHTMLDownload(df)

    Thesis(df)

if __name__ == '__main__':
    main()
