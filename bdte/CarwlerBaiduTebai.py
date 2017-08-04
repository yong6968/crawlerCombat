import urllib;
import urllib.request;
import re

#百度贴吧爬虫类
class CarwlerBaiduTebai:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
    # 传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url);
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print (u"连接百度贴吧失败,错误原因", e.reason)
                return None
    # 获取标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
    #提取帖子页数
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
     # 获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        pageStories = []
        for item in items:
            pageStories.append(item)
        return pageStories

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = CarwlerBaiduTebai(baseURL,1)
print(bdtb.getContent(bdtb.getPage(1)))