#!/usr/bin/python3
#_*_coding:UTF-8 _*_


from urllib import request
from http import cookiejar
from urllib import parse


class MovieTop(object):
    #初始化数据
    def _init_(self):
        self.start=0
        self.param='&filter='
        #self.headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/51.0.2704.63 Safari/537.36'}

    #获取页面数据
    def get_page(self):
        page_content=[]
        try:
            while self.start<=225:
                url='http://movie.douban.com/top250?start='+str(self.start)
                req=request.Request(url,headers=self.headers)
                response=request.urlopen(req)
                data=response.read()
                self.saveFile(data)
                page=data.decode('utf-8')
                page_num=(self.start+25)//5
                print('正在抓取第'+str(page_num)+'页数据...')
                self.start+=25
                page_content.append(page)
                return page_content
        except request.URLError as e:
            if hasattr(e,'reason'):
                print('抓取失败，失败原因：',e.reason)

    #保存文件到本地函数
    def saveFile(self,data=None):
        path = "E:\\douban.out"
        f= open(path,'wb')
        f.write(data)
        f.close
        
    #调度内部函数
    def main(self):
        print('开始从豆瓣电影抓取数据：')
        self.get_page()
        print("数据抓取完毕...")

t=MovieTop()
t._init_()
t.main()
