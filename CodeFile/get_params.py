import requests

#將參數定義為字典資料

payload = {'key':'value1','key2':'value2'}
html = requests.get("https://httpbin.org/get",params = payload)
print(html.text)
