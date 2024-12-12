import requests
url = 'https://httpbin.org/get'
html = requests.get(url)
# 檢查HTTP回應碼是否為 200 (成功連接request.code.ok)
if html.status_code == requests.codes.ok:
    print(html.text)