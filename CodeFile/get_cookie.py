import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index1.html'

#設定 cookies 的值
cookies ={'over18':'1'}

r = requests.get(url,cookies = cookies)
print(r.text)