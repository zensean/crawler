import urllib.request as req
# 使用內建 Json 套件,協助我們解析 Json 格式資料 
import json 
# 抓取目標頁面文章資料
url="https://medium.com/_/graphql"
# 建立一個 request 物件, 附加 request headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
})

# 根據觀察, 取得的資料是 Json 格式
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") 
    
# 解析 Json 格式的資料, 取得每篇文章的標題
# 把原始的 Json 資料解析成字典/列表的表示形式
# data=data.replace("[","")
data=json.loads(data)
print(data)