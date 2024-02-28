項目名稱：提取文章標題的網路爬蟲

描述：
該項目涉及使用網路爬蟲從不同來源提取文章標題。 專案中包含三個不同的腳本：

提取Medium文章標題： 此腳本使用GraphQL查詢從Medium.com提取文章標題。 它利用urllib函式庫發送請求，並使用json函式庫解析JSON回應。 提取的標題隨後列印到控制台。

PTT電影板塊爬蟲： 此腳本從PTT（批踢踢實業坊）論壇的電影板塊中提取文章標題。 它使用urllib取得網頁，並使用BeautifulSoup解析HTML內容。 提取的標題在提取後列印到控制台。

帶有分頁的PTT八卦板塊爬蟲： 此腳本從PTT論壇的八卦板塊中提取文章標題，並支援分頁。 它迭代多個頁面以獲取每個頁面的標題。 類似PTT電影板塊爬蟲，它使用urllib獲取頁面，並使用BeautifulSoup解析HTML內容。 它會列印出每個頁面的標題，並繼續到下一個頁面，直到爬取到指定數量的頁面為止。

包含的文件：

medium_article_titles.py：從Medium.com擷取文章標題的腳本。
ptt_movie_board_scraper.py：從PTT電影板塊爬取文章標題的腳本。
ptt_gossiping_board_scraper_with_pagination.py：支援分頁從PTT八卦板塊爬取文章標題的腳本。
README.md：該檔案提供了專案的概述，包括每個腳本的描述以及如何執行它們的說明。
如何使用：
可以單獨運行每個腳本以從相應來源獲取文章標題。 確保在系統上安裝了Python，並安裝了諸如urllib、json和BeautifulSoup之類的依賴項。

要運行每個腳本：

開啟終端機或命令提示字元。
導航到包含腳本的目錄。
使用指令python script_name.py運行腳本。
注意事項： 在執行腳本時確保有良好的網路連接，以從網路來源取得資料。 此外，請尊重被爬取網站的服務條款和使用政策。


Project Name: Web Scraping for Article Titles

Description:
This project involves web scraping to extract article titles from various sources. Three different scripts are provided within this project:

Medium Article Titles Retrieval: This script retrieves article titles from Medium.com using GraphQL queries. It utilizes the urllib library to send requests and the json library to parse the JSON response. The extracted titles are then printed to the console.

PTT Movie Board Scraper: This script scrapes article titles from the Movie board of the PTT (批踢踢實業坊) forum. It uses urllib for fetching web pages and BeautifulSoup for parsing HTML content. The titles are printed to the console after extraction.

PTT Gossiping Board Scraper with Pagination: This script scrapes article titles from the Gossiping board of the PTT forum with pagination support. It iterates over multiple pages to gather titles from each page. Similar to the PTT Movie Board Scraper, it employs urllib for fetching pages and BeautifulSoup for parsing HTML content. It prints out titles from each page and proceeds to the next page until a specified number of pages are scraped.

Files Included:

medium_article_titles.py: Script to retrieve article titles from Medium.com.
ptt_movie_board_scraper.py: Script to scrape article titles from the PTT Movie board.
ptt_gossiping_board_scraper_with_pagination.py: Script to scrape article titles from the PTT Gossiping board with pagination support.
README.md: This file provides an overview of the project, including descriptions of each script and instructions on how to run them.
How to Use:
Each script can be run individually to fetch article titles from the respective sources. Ensure Python is installed on your system, and dependencies like urllib, json, and BeautifulSoup are installed.

To run each script:

Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script using the command python script_name.py.
Note: Ensure that you have proper internet connectivity while running the scripts to fetch data from the web sources. Additionally, respect the terms of service and usage policies of the websites being scraped.
