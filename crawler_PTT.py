import urllib.request as req
import bs4
# 抓取目標頁面原始碼(html)
url="https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 request 物件, 附加 request headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"fMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

# 解析原始碼, 取得每篇文章的標題
root=bs4.BeautifulSoup(data, "html.parser")
# 輸出<title>的文字
# print(root.title.string)
# 尋找 class="title" 的 div標籤
titles=root.find("div", class_="title")
# 輸出 titles中 <a>裡面的字串
print(titles.a.string)

# 尋找所有 class="title" 的 div標籤
titles=root.find_all("div", class_="title")

for title in titles:
    # 如果標題包含<a>標籤 (沒有被刪除), 則逐個印出來
    if title.a != None:
        print(title.a.string)