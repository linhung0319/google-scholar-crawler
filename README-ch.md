# google-scholar-crawler

<div markdown>
  
  🌏
  [**English**](https://github.com/linhung0319/google-scholar-crawler/README.md) |
  Chinese |
  
</div>

>這是我練習寫的一個爬取[Google Scholar Search Page](https://scholar.google.com.tw)的網路爬蟲程式
>
>１. 將Google Search Page上，Paper的標題，年份和網址['title', 'year', 'url']，以CSV檔案格式記錄下來
>
>２. 將Google Search Page上，含有Tag (如[PDF], [HTML])的連結，以PDF檔案格式下載下來

## Get Started

>本程式適用於mac，以Python 2.7.10執行，使用函式庫requests, BeautifulSoup, pdfkit，建議皆以pip安裝
>
>安裝pdfkit前，需要下載[wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

在Terminal下載程式碼

```
$ git clone https://github.com/linhung0319/google-scholar-crawler.git
```

## How to Use

### 1. 前往[Google Scholar Search](https://scholar.google.com.tw)

輸入你想找的關鍵字，到達Search Page的第一頁，並複製此頁的網址

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/page.png)

### 2. 進入google_crawler.py

將複製的網址放入start_url， start_url = '網址'

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/url.png)

### 3. p_key放入想找的關鍵字，n_key放入不想找的關鍵字

在Search Page中，每一格的標題和內容，若含有p_key中的字，則Crawler會傾向於抓取此篇Paper

在Search Page中，每一格的標題和內容，若含有n_key中的字，則Crawler會傾向於忽略此篇Paper

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/key.png)

在上圖中，因為我想找跟聲音相關，不想找跟光學相關的Paper，所以p_key中放入跟聲音相關的字，n_key中放入跟光學相關的字

### 4. 設定 page = 數字 ，可以設定要抓取幾頁的Google Search Page

![](https://github.com/linhung0319/google-scholar-crawler/blob/master/set.png)

設定太多頁會誘發Google的robot check

### 5. 開始執行程式

在Terminal中執行 google_crawler.py

```
$ python google_crawler.py
```

會將抓取的資料 ('title', 'year', 'url',...) ,存在result.pickle中

然後，在Terminal中執行 csvNdownload.py

```
$ python csvNdownload.py
```

將資料轉為CSV檔，存入CSV資料夾

下載具有Tag (PDF, HTML)的連結轉為PDF檔，分別存入PDF，HTML資料夾

## Google Robot Check

Google Search Page 會進行反爬蟲偵測，如果下載或是觀看網頁的手速太快，他會懷疑你是機器人，並且禁止掉你的IP位址

目前想到的最簡單的方法，是使用VPN，當被認為是機器人，就使用VPN馬上改變自己的IP位址

現在網路上有許多的免費VPN可以下載

若在跑Crawler的時候出現訊息

```
__findPages - Can not find the pages link in the start URL!!
__findPages - 1.Google robot check might ban you from crawling!!
__findPages - 2.You might not crawl the page of google scholar

```

解決方式為使用VPN，轉換IP

## Contact Information
如果你有任何任何問題或建議，請由此聯繫我:
- Email: linhung0319@gmail.com
- Portfolio: [My Portfolio](https://linhung0319.vercel.app/)
- Linkedin: [My Linkedin](https://www.linkedin.com/in/hung-lin/)
