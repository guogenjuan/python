#!/usr/bin/python3
#_*_coding:UTF-8 _*_

from urllib import request
from http import cookiejar
from urllib import parse


#cookie处理
#cookie_support = request.HTTPCookieProcessor(cookiejar.CookieJar())
#opener = request.build_opener(cookie_support,request.HTTPHandler)

#使用代理服务器
#proxy_support = request.ProxyHandler({'http':'61.135.217.7:80'})
#opener = request.build_opener(proxy_support,request.HTTPHandler)

#request.install_opener(opener)
#response = request.urlopen("http://movie.douban.com/")
#content = response.read().decode('utf-8')
#print(content)

#伪装成浏览器
headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


#构造请求数据(报类型错误要进行格式转换)
#postdata = parse.urlencode({}).encode('utf-8')
postdata = parse.urlencode({
'username':'13636488463','password':'juan@871378','continueURL':'http://www.verycd.com/','fk':'dfafafaf','login_submit':'登录'}).encode('utf-8')

#构造数据放入请求中
req=request.Request(url='https://zhihu.com',data=postdata,headers=headers)

response=request.urlopen(req)
content = response.read().decode('utf-8')

print(content)









