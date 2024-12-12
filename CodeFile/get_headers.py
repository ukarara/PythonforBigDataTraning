
import requests
url = 'https://www.thsrc.com.tw/'

#自訂標頭
headers ={
    'user-agent':'Mozilla/5.0(windows NT 10.0;win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/64.0.3282.186 Safari/537.36'
}
#將自訂標投加入get請求中
html = requests.get(url,headers = headers)
print(html)