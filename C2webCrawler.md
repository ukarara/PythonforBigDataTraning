# C2 數據資料的爬取（WEB　Crawler/Spyder）
## 

## Request 模組

### 發送Get請求
網站內容: https://httpbin.org/get

![httpbin.org_get網站內容](img/httpbin.org_get.PNG)

* get.py

```
import requests
url = 'https://httpbin.org/get'
html = requests.get(url)
# 檢查HTTP回應碼是否為 200 (成功連接request.code.ok)
if html.status_code == requests.codes.ok:
    print(html.text)

```
![get.py](img/get.PNG)


* get_params.py


  ```https://www.test.com/x=value1&y=value2```

  * URL參數與網址用 '?' 做串接，多參數用 '&' 。

  * 在Request模組中，URL參數要用字典資料型態定義，用GET請求時必須將URL參數加入Params參數，即可執行。
```
import requests

#將參數定義為字典資料

payload = {'key':'value1','key2':'value2'}
html = requests.get("https://httpbin.org/get",params = payload)
print(html.text)

```
![get_params.py結果](img/get_params.png)

### 發送Post請求
post請求是常用的HTTP請求，只要網頁內有讓使用者輸入的表單，都會需要POST請求來進行傳送。

在requests模組中，POST傳送的參數需要定義成字典資料型態，接著用POST請求將傳遞的參數內容設定為DATA參數，即可完成。

* POST.py
```
import requests
# 將查詢參數加入POST請求中

payload = {'key':'value1','key2':'value2'}
html = requests.post("https://httpbin.org/post",data = payload)
print(html.text)

```
![POST.py結果](img/POST.png)

### 自訂 HTTP Headers 偽裝瀏覽器操作

HTTP Headers是HTTP請求和回應的核心，其中標示了用戶端瀏覽器、請求頁面、伺服器等相關資訊。
進階的網路爬蟲程式中，自訂HTTP Headers可以將爬取的動作偽裝成瀏覽器的操作，避過網頁檢查。
設定方式為在headers設定user-agent屬性。

* get_headers.py
```
#get_headers.py
import requests
url = 'https://www.thsrc.com.tw/'

#自訂標頭
headers ={
    'user-agent':'Mozilla/5.0(windows NT 10.0;win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/64.0.3282.186 Safari/537.36'
}
#將自訂標投加入get請求中
html = requests.get(url,headers = headers)
print(html)
```
![get_headers.py結果](img/get_headers.png)

`<Response [200]>`
回應HTTP狀態碼為200代表正確讀取。如果不加自訂的HAEADERS設定，程式會卡住無法正確執行。

### 使用 Session 及 Cookie 進入認證頁面

* 在網頁的開發者工具中(F12-應用程式-儲存空間-Cookie)，找到Cookie。
![pttCookie](img/pttCookie.png)

當用戶端瀏覽器訪問伺服器端瀏覽器時，伺服器會發給用戶端一個憑證以供識別，這個憑證儲存在用戶端的瀏覽器中就是 Cookie ，產生在伺服器端的就是 Session。當下次在拜訪該網站時，只要所屬的 Cookie 跟 Session 還沒過期，伺服器就能辨識，提供程式進一步使用。

在進階網路爬蟲中，若目標頁面需要Cookie值認證，會因為這個機制干擾導致讀取失敗。解決方法就是在進行請求時加入 Cookie。



在requests請求中加入 cookies 的參數，cookie的參數必須為字典。

*get_cookie.py
```
import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index1.html'

#設定 cookies 的值
cookies ={'over18':'1'}

r = requests.get(url,cookies = cookies)
print(r.text)
#就會正確印出網站內容

```

## BeautifulSoup 的使用

BeautifulSoup 模組可快速提取HTML的內容，只要對網頁結構有基礎的了解，即可透過一定邏輯取出複雜頁面的指定資料。

bsdemo1.htm
```
<!doctype html>
<html lang="zh">
  <head>
    <meta charset="UTF-8">
    <title>我是網頁標題</title>
  </head>
  <body>
    <h1 class="large">我是標題</h1>
    <div>
      <p>我是段落</p>
      <img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_256.png" alt="我是圖片">
      <a href="http://www.e-happy.com.tw">我是超連結</a>
    </div>
  </body>
</html>

```
載入 BeautifulSoup 後，同時利用 requests 模組取得網頁原始碼，就可以使用PYTHON內建的html.parser 或 lxml解析器解析原始碼，建立 BeautifulSoup 物件後再進行解析。
```
from bs4 import BeautifulSoup
BeautifulSoup 物件  = BeautifulSoup(原始碼，解析器)
```

* 解析器

|BeautifulSoup(原始碼，html.parser)|PYTHON內建，執行速度適中文件容錯能力強，|
| ----------- | ------- |
|BeautifulSoup(原始碼，lxml)|執行速度快，文件容錯強|


### BeautifulSoup 常用屬性

| 屬性     | 說明                                             |
|----------|--------------------------------------------------|
| 標籤名稱 | 傳回指定標籤內容，例如sp.title，傳回的標籤內容。 |
| text     | 傳回去除所有HTML標籤後的網頁文字內容。           |

建立 BeautifulSoup 型別物件 sp，解析 http://ehappy.tw/bsdemo1.htm 網頁原始碼。接著用 標籤名稱 與 text 2個屬性取出指定資料。

*bs1.py
```
import requests
from bs4 import BeautifulSoup
url = 'http://ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')
print(sp.title)
print(sp.title.text)
print(sp.H1)
print(sp.p)
```

在HTML中每個標籤都為DOM結構中的節點，使用 BeautifulSoup 物件.標籤名稱即可取得該節點中的內容(包含HTML標籤)。為取得內容加入text屬性，可去除HTML標籤，取得標籤區域內文字。
![bs1.py結果](img/bs1.png)