import re
import requests
from bs4 import BeautifulSoup
from tqdm import trange
import time
print("hello")
#头部伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
url = "https://www.uukanshu.com/b/92/17638.html"
req = requests.get(url,headers=headers)
req.encoding = 'utf8'
html = req.text
data = BeautifulSoup(html,"html.parser")

section_name = data.title.string
print(section_name)