import requests
# 將查詢參數加入POST請求中

payload = {'key':'value1','key2':'value2'}
html = requests.post("https://httpbin.org/post",data = payload)
print(html.text)