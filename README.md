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
