import urllib
import urllib.request
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent':user_agent}
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class' +
                         '="content.*?>(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',
                         re.S)
    items = re.findall(pattern,content)
    # print(items)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print(item[0],item[1],item[2])
except urllib.request.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)