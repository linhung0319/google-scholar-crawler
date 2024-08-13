# google-scholar-crawler

<div markdown>
  
  🌏
  English |
  [**Chinese**](https://github.com/linhung0319/google-scholar-crawler/README-ch.md) |
  
</div>

>This is a web scraping program I wrote to practice extracting data from [Google Scholar Search Pages](https://scholar.google.com.tw).
>
>１. It records the titles, publication years, and URLs ['title', 'year', 'url'] of papers on the Google Search Page in a CSV file format.
>
>２. It downloads links on the Google Search Page that contain tags (such as [PDF], [HTML]) in PDF file format.

## Get Started

>This program is designed for macOS and runs on Python 2.7.10. It uses the requests, BeautifulSoup, and pdfkit libraries, all of which are recommended to be installed via pip.
>
>Before installing pdfkit, you need to download [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

Clone the code in the terminal

```
$ git clone https://github.com/linhung0319/google-scholar-crawler.git
```

## How to Use

### 1. Go to [Google Scholar Search](https://scholar.google.com.tw)

Enter the keywords you want to search for, navigate to the first page of the search results, and copy the URL of this page.

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/page.png)

### 2. Go to google_crawler.py

Paste the copied URL into the start_url variable like this: start_url = 'URL'.

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/url.png)

### 3. Set p_key for keywords you want to include and n_key for keywords you want to exclude

In the Search Page, if the title and content of an entry contain words from p_key, the crawler will be inclined to scrape that paper.

If the title and content of an entry contain words from n_key, the crawler will be inclined to ignore that paper.

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/key.png)

In the example shown above, because I wanted to find papers related to sound but not optics, I included sound-related words in p_key and optics-related words in n_key.

### 4. Set page = number to specify the number of Google Search Pages you want to scrape

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/set.png)

Setting too many pages may trigger Google’s robot check.

### 5. Run the program

Run google_crawler.py in the Terminal.

```
$ python google_crawler.py
```

The scraped data ('title', 'year', 'url', etc.) will be saved in result.pickle.

Run csvNdownload.py in the Terminal.

```
$ python csvNdownload.py
```

This will convert the data to a CSV file, saved in the CSV folder.

It will also download links with tags (PDF, HTML) as PDF files and save them in the PDF and HTML folders, respectively.

## Google Robot Check

Google Search Pages have anti-scraping detection. If you download or view pages too quickly, they may suspect you are a bot and block your IP address.

The simplest solution I can think of is to use a VPN. If you are flagged as a bot, you can quickly change your IP address using the VPN.

There are many free VPNs available for download online.

If you encounter a message while running the crawler, the solution is to use a VPN to change your IP.

```
__findPages - Can not find the pages link in the start URL!!
__findPages - 1.Google robot check might ban you from crawling!!
__findPages - 2.You might not crawl the page of google scholar

```

## Contact Information
If you have any questions or suggestions about this project, feel free to contact me:
- Email: linhung0319@gmail.com
- Portfolio: [My Portfolio](https://linhung0319.vercel.app/)
- Linkedin: [My Linkedin](https://www.linkedin.com/in/hung-lin/)
